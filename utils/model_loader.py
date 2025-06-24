import os
from dotenv import load_dotenv
from config.config_loader import load_config
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

class ModelLoader:
    '''
    A utility class to load embedding and LLM models
    '''
    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config = load_config()

    def _validate_env(self):
        '''
        Validate necessary environment variables
        '''  
        required_vars = ["OPENAI_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {missing_vars}")

    def load_embedding_model(self):
        '''
        Load embedding model
        '''
        print("Loading embedding model...")
        model_name = self.config["embedding_model"]["model_name"]
        return OpenAIEmbeddings(model=model_name)

    def load_llm_model(self):
        '''
        Load LLM model
        '''
        print("Loading LLM model...")
        model_name = self.config["llm"]["model_name"]
        openai_model =ChatOpenAI(model=model_name)

        return openai_model