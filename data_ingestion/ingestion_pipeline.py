import os
import sys
import pandas as pd
from dotenv import load_dotenv
from typing import List, Tuple
from langchain_core.documents import Document
from langchain_community.vectorstores import AstraDB as AstraDBVectorStore

# Add the parent directory to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.model_loader import ModelLoader
from config.config_loader import load_config

class DataIngestion:
    """
    Class to handle data transformation and ingestion into AstraDB vector store.
    """

    def __init__(self):
        """
        Initialize environment variables, embedding model, and set CSV file path.
        """
        print("Initializing DataIngestion pipeline...")
        self.model_loader = ModelLoader()
        self._load_env_variables() #the method starting with _ is private method
        self.csv_path = self._get_csv_path()
        self.product_data = self._load_csv()
        self.config = load_config()

    def _load_env_variables(self):
        """
        Load and validate required environment variables.
        """
        load_dotenv()
        
        required_vars = ["OPENAI_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
        
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.db_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
        self.db_application_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
        self.db_keyspace = os.getenv("ASTRA_DB_KEYSPACE")

    def _get_csv_path(self):
        """
        Get path to the CSV file located inside 'data' folder.
        """
        current_dir = os.getcwd()
        csv_path = os.path.join(current_dir, 'data', 'flipkart_product_review.csv')

        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at: {csv_path}")

        return csv_path

    def _load_csv(self):
        """
        Load product data from CSV.
        """
        df = pd.read_csv(self.csv_path)
        expected_columns = {'product_title', 'rating', 'summary', 'review'}

        if not expected_columns.issubset(set(df.columns)):
            raise ValueError(f"CSV must contain columns: {expected_columns}")

        return df
        
    def clear_all_data(self):
        """
        Delete all data from the vector store collection
        """
        try:
            # Create vector store connection
            collection_name = self.config["astra_db"]["collection_name"]
            vstore = AstraDBVectorStore(
                embedding=self.model_loader.load_embedding_model(),
                collection_name=collection_name,
                api_endpoint=self.db_api_endpoint,
                token=self.db_application_token,
                namespace=self.db_keyspace,
            )
            
            print("🗑️ Attempting to clear all data from AstraDB collection...")
            
            # Method 1: Try using the clear method if available
            if hasattr(vstore, 'clear'):
                vstore.clear()
                print("✅ Successfully cleared all data using clear() method")
                return True
            
            # Method 2: Try to delete collection using AstraDB client
            elif hasattr(vstore, 'astra_db') and hasattr(vstore.astra_db, 'delete_collection'):
                vstore.astra_db.delete_collection(collection_name)
                print(f"✅ Successfully deleted collection '{collection_name}'")
                return True
            
            # Method 3: Try to delete using delete_by_query if available
            elif hasattr(vstore, 'delete_by_query'):
                vstore.delete_by_query({})  # Empty query should match all documents
                print("✅ Successfully deleted all documents using delete_by_query")
                return True
                
            else:
                print("❌ No direct clear method available. Unable to clear data.")
                return False
                
        except Exception as e:
            print(f"❌ Error clearing data: {e}")
            return False

    def check_if_data_exists(self, vstore):
        """
        Check if data already exists in the vector store
        """
        try:
            results = vstore.similarity_search("test", k=1)
            return len(results) > 0
        except Exception as e:
            print(f"Error checking data existence: {e}")
            return False

    def transform_data(self):
        """
        Transform product data into list of LangChain Document objects.
        """
        product_list = []

        for _, row in self.product_data.iterrows():
            product_entry = {
                "product_name": row['product_title'],
                "product_rating": row['rating'],
                "product_summary": row['summary'],
                "product_review": row['review']
            }
            product_list.append(product_entry)

        documents = []
        for entry in product_list:
            metadata = {
                "product_name": entry["product_name"],
                "product_rating": entry["product_rating"],
                "product_summary": entry["product_summary"]
            }
            doc = Document(page_content=entry["product_review"], metadata=metadata)
            documents.append(doc)

        print(f"Transformed {len(documents)} documents.")
        return documents

    def store_in_vector_db(self, documents: List[Document]):
        """
        Store documents into AstraDB vector store.
        """
        collection_name = self.config["astra_db"]["collection_name"]
        vstore = AstraDBVectorStore(
            embedding=self.model_loader.load_embedding_model(),
            collection_name=collection_name,
            api_endpoint=self.db_api_endpoint,
            token=self.db_application_token,
            namespace=self.db_keyspace,
        )

        inserted_ids = vstore.add_documents(documents)
        print(f"Successfully inserted {len(inserted_ids)} documents into AstraDB.")
        return vstore, inserted_ids

    def run_pipeline(self):
        """
        Smart pipeline: check if data exists, insert only if needed, always show search results.
        """
        # First create vector store connection to check for existing data
        collection_name = self.config["astra_db"]["collection_name"]
        vstore = AstraDBVectorStore(
            embedding=self.model_loader.load_embedding_model(),
            collection_name=collection_name,
            api_endpoint=self.db_api_endpoint,
            token=self.db_application_token,
            namespace=self.db_keyspace,
        )

        # Check if data already exists
        if self.check_if_data_exists(vstore):
            print("✅ Data already exists in vector store. Skipping insertion.")
        else:
            print("📥 No data found. Inserting fresh data...")
            documents = self.transform_data()
            inserted_ids = vstore.add_documents(documents)
            print(f"Successfully inserted {len(inserted_ids)} documents into AstraDB.")

        # Always do a search and show results (regardless of whether data was inserted or not)
        query = "Can you tell me the low budget headphone?"
        results = vstore.similarity_search(query)

        print(f"\nSample search results for query: '{query}'")
        for res in results:
            print(f"Content: {res.page_content}\nMetadata: {res.metadata}\n")

# Run if this file is executed directly
if __name__ == "__main__":
    ingestion = DataIngestion()
    
    # First, clear all existing data to remove duplicates
    print("🔄 STEP 1: Clearing all existing data from AstraDB to remove duplicates...")
    ingestion.clear_all_data()
    
    # Then run the pipeline once to insert fresh data
    print("\n🔄 STEP 2: Running pipeline to insert fresh data...")
    ingestion.run_pipeline()