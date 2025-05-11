import os

class Settings:
    # Example: Load settings from environment variables
    AZURE_AGENT_API_KEY = os.getenv('AZURE_AGENT_API_KEY', '')
    AZURE_CONTENT_UNDERSTANDING_ENDPOINT = os.getenv('AZURE_CONTENT_UNDERSTANDING_ENDPOINT', '')
    # Add more configuration as needed

settings = Settings()
