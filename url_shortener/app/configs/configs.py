from dataclasses import dataclass
from dotenv import find_dotenv, load_dotenv
from os import getenv

@dataclass
class Configs:
    """
    Configuration class to hold all the configurations for the application.
    """

    # Load environment variables from .env file
    load_dotenv(find_dotenv())

    # Database configuration
    DB_HOST: str = getenv("DB_HOST", "localhost")
    DB_PORT: int = int(getenv("DB_PORT", 5432))
    DB_NAME: str = getenv("DB_NAME", "your_database_name")
    DB_USER: str = getenv("DB_USER", "your_database_user")
    DB_URL: str = getenv("DB_URL", "your_database_url")
    DB_PASSWORD: str = getenv("DB_PASSWORD", "your_database_password")

    # Other configurations can be added here

    # Example: API keys, secret keys, etc.
    def __init__(self):
        """
        Initialize the configuration class.
        """
        pass