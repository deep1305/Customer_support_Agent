import os
import sys
from langchain_astradb import AstraDBVectorStore
from typing import List
from langchain_core.documents import Document
from dotenv import load_dotenv

# Add the parent directory to Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from utils.config_loader import load_config
from utils.model_loader import ModelLoader

class Retriever:
    
    def __init__(self):
        self.model_loader = ModelLoader()
        self.config = load_config()
        self._load_env_variables()
        self.vstore = None
        self.retriever = None
    
    def _load_env_variables(self):
         
        load_dotenv()
         
        required_vars = ["OPENAI_API_KEY", "ASTRA_DB_API_ENDPOINT", "ASTRA_DB_APPLICATION_TOKEN", "ASTRA_DB_KEYSPACE"]
        
        missing_vars = [var for var in required_vars if os.getenv(var) is None]
        
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.db_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
        self.db_application_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
        self.db_keyspace = os.getenv("ASTRA_DB_KEYSPACE")
        
    
    def load_retriever(self):
        if not self.vstore:
            collection_name = self.config["astra_db"]["collection_name"]
            
            self.vstore = AstraDBVectorStore(
                embedding=self.model_loader.load_embedding_model(),
                collection_name=collection_name,
                api_endpoint=self.db_api_endpoint,
                token=self.db_application_token,
                namespace=self.db_keyspace,
            )
        if not self.retriever:
            top_k = self.config["retriever"]["top_k"] if "retriever" in self.config else 3
            self.retriever = self.vstore.as_retriever(search_kwargs={"k": top_k})
            print("Retriever loaded successfully.")
        return self.retriever
   

    
    def call_retriever(self, query: str) -> List[Document]:
        retriever = self.load_retriever()
        output = retriever.invoke(query)
        return output
        
    
if __name__ == '__main__':
    retriever_obj = Retriever()
    user_query = "Can you suggest good budget laptops?"
    results = retriever_obj.call_retriever(user_query)

    for idx, doc in enumerate(results, 1):
        print(f"Result {idx}: {doc.page_content}\nMetadata: {doc.metadata}\n")