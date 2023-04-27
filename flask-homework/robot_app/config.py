import os
from dotenv import load_dotenv

load_dotenv()
class AppConfig:
    DEBUG = os.getenv('DEBUG')
    HOST = os.getenv('0.0.0.0')
    PORT = os.getenv('PORT')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')