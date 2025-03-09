# from dotenv import load_dotenv
import os

# Load environment variables
# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DATABASE = os.getenv("DATABASE")
# DB_HOST = os.getenv("DB_HOST")

#comment ankushsasdfaskgask

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DATABASE = os.environ["DATABASE"]
DB_HOST = os.environ["DB_HOST"]


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
