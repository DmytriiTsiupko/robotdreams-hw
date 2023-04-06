from flask import Flask
from logging.config import dictConfig
from .config import AppConfig


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }}
})


app = Flask(__name__)


app.config.from_object(AppConfig)


from .views import *
