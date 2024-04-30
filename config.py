from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.environ.get("DATABASE")
DB_USER = os.environ.get("USER")
DB_PASSWORD = os.environ.get("PASSWORD")
DB_HOST = os.environ.get("HOST")
DB_PORT = os.environ.get("PORT")

TOKEN = os.environ.get("TOKEN_API")
