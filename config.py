import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tessa.db")
    PORT = int(os.getenv("PORT", 8000))
    FLASK_ENV = os.getenv("FLASK_ENV", "development")