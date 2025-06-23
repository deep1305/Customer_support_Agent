import pandas as pd
import os
from pathlib import Path
from langchain_core.documents import Document


class data_conversion:
    # Define the specific file this class should work with
    REQUIRED_FILE = "amazon_product_review.csv"
    
    def __init__(self):
        print("data_conversion class initialized")
        print(f"This class is designed specifically for: {self.REQUIRED_FILE}")
        
        self.file_path = self._find_file(self.REQUIRED_FILE)
        
        if self.file_path:
            print(f"Found required file at: {self.file_path}")
            self.product_data = pd.read_csv(self.file_path)
            #print(self.product_data.head())
        else:
            raise FileNotFoundError(f"Required file '{self.REQUIRED_FILE}' not found in project directory or subdirectories")

    def _find_file(self, filename):
        """
        Search for the specific required file in the current directory and all subdirectories
        Returns the full path if found, None otherwise
        """
        # Get the project root directory (where this script is being run from)
        project_root = Path.cwd()
        
        print(f"Searching for '{filename}' in '{project_root}' and subdirectories...")
        
        # Search in current directory and all subdirectories
        for file_path in project_root.rglob(filename):
            if file_path.is_file():
                print(f"Required file found: {file_path}")
                return str(file_path)
        
        # If not found in project root, try looking from the script's directory
        script_dir = Path(__file__).parent.parent  # Go up one level from data_ingestion
        print(f"Also searching from script directory: {script_dir}")
        
        for file_path in script_dir.rglob(filename):
            if file_path.is_file():
                print(f"Required file found: {file_path}")
                return str(file_path)
        
        return None

    def list_csv_files(self):
        """
        Helper method to list all CSV files in the project
        Useful for debugging when the required file is not found
        """
        project_root = Path.cwd()
        csv_files = list(project_root.rglob("*.csv"))
        
        if csv_files:
            print("Available CSV files in project:")
            for csv_file in csv_files:
                if csv_file.name == self.REQUIRED_FILE:
                    print(f"  ✅ {csv_file} (REQUIRED FILE)")
                else:
                    print(f"  ❌ {csv_file} (different purpose)")
        else:
            print("No CSV files found in project directory")
        
        return csv_files

    def get_required_filename(self):
        """
        Returns the specific filename this class is designed to work with
        """
        return self.REQUIRED_FILE
    

    def data_transformation(self):
        required_cols = self.product_data.columns
        required_cols = list(required_cols[1:])
        # print(required_cols)

        product_list = []

        for index, row in self.product_data.iterrows():
            product_dict = {
                "product_name": row['product_title'],
                "product_rating": row['rating'],
                "product_summary": row['summary'],
                "product_review": row['review']
            }
            product_list.append(product_dict)
        #print("-------------Below is the product data list-------------")
        #print(product_list)
        
        docs = []
        for entry in product_list:
            metadata = {
                "product_name": entry['product_name'],
                "product_rating": entry['product_rating'],
                "product_summary": entry['product_summary']
                
            }
            document = Document(page_content=entry['product_review'], metadata=metadata)
            docs.append(document)
        #print(docs[1])
        return docs

if __name__ == "__main__":
    try:
        # Only works with the specific required file
        data_convert = data_conversion()
        data_convert.data_transformation()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"\nThis class specifically needs: {data_conversion.REQUIRED_FILE}")
        print("\nLet me show you what CSV files are available:")
        temp_instance = data_conversion.__new__(data_conversion)  # Create instance without __init__
        temp_instance.REQUIRED_FILE = data_conversion.REQUIRED_FILE
        temp_instance.list_csv_files()
        
        print(f"\nTo fix this:")
        print(f"1. Make sure '{data_conversion.REQUIRED_FILE}' exists in your project")
        print(f"2. Place it in the 'data/' folder or any subdirectory")
        print(f"3. Check the filename spelling exactly: '{data_conversion.REQUIRED_FILE}'")