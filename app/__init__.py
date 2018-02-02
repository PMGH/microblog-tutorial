from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# __name__ is a predifined python variable - set to the name of the module in which it is used.
# Flask uses the module passed (__name__) as the application start point when it needs to load associated resources.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# importing at the bottom is a workaround for circular imports - a common problem with Flask applications
from app import routes, models
