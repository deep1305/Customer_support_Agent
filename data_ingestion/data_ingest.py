from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
load_dotenv()

import os
import pandas as pd
from data_ingestion.data_transform import data_conversion
from langchain_openai import OpenAIEmbeddings

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["ASTRA_DB_API_ENDPOINT"] = os.getenv("ASTRA_DB_API_ENDPOINT")
os.environ["ASTRA_DB_KEYSPACE"] = os.getenv("ASTRA_DB_KEYSPACE")
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = os.getenv("ASTRA_DB_APPLICATION_TOKEN")


class ingest_data:
    def __init__(self):
        print("ingest_data class initialized")
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.data_conversion = data_conversion()
        self.vstore = None

    def get_vector_store(self):
        """Get or create vector store connection"""
        if self.vstore is None:
            self.vstore = AstraDBVectorStore(
                embedding=self.embeddings,
                collection_name="chatbot_ecommerce",
                api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
                token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
                namespace=os.getenv("ASTRA_DB_KEYSPACE")
            )
        return self.vstore

    def check_if_data_exists(self):
        """Check if data already exists in the vector store"""
        try:
            vstore = self.get_vector_store()
            # Try a simple search to see if there are any documents
            results = vstore.similarity_search("test", k=1)
            return len(results) > 0
        except Exception as e:
            print(f"Error checking data existence: {e}")
            return False

    def insert_data_once(self):
        """Insert data only if it doesn't already exist"""
        if self.check_if_data_exists():
            print("Data already exists in vector store. Skipping insertion.")
            return self.get_vector_store(), None
        else:
            print("No data found. Inserting new data...")
            vstore = self.get_vector_store()
            docs = self.data_conversion.data_transformation()
            inserted_ids = vstore.add_documents(docs)
            print(f"Inserted {len(inserted_ids)} documents.")
            return vstore, inserted_ids


if __name__ == "__main__":
    ingest_data = ingest_data()
    vstore, inserted_ids = ingest_data.insert_data_once()
    
    results = vstore.similarity_search("can you tell me high budget headphones")
    for res in results:
        print(f'{res.page_content} {res.metadata}')
        print("-" * 50)
        