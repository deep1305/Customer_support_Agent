from setuptools import setup, find_packages

# This setup.py file is used to make the project installable as a Python package.
# It allows you to:
# 1. Install the project in development mode with "pip install -e ."
# 2. Define project metadata and dependencies
# 3. Make the project's modules importable from anywhere
# 4. Package and distribute the project if needed

setup(name = "e-commerce-bot",
      version = "0.0.1",
      author = "deep",
      author_email = "shahdeep1399@gmail.com",
      packages = find_packages(),
      install_requires = ["langchain_astradb", "langchain_community", "langchain", "fastapi", "pandas", "python-dotenv"]
)