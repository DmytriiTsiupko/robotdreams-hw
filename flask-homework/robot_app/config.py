import os
from dotenv import load_dotenv

load_dotenv()
class AppConfig:
    DEBUG = os.getenv('DEBUG')
    HOST = os.getenv('0.0.0.0')
    PORT = os.getenv('PORT')
