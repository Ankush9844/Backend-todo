from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

database_url = os.getenv("DATABASE_URL")

class Config:
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
