from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#app instance
app = Flask(__name__)

#Config
app.config["SECRET_KEY"] = "sadhfr2e9u8euhisuhd"  #For more security, use .env file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

#database instance
db = SQLAlchemy(app)

# Uncomment to create database
# from src.models import PreRating, PostRating, WatchVideo
# with app.app_context():
#     db.create_all()


#import routes so flask can find them
from src import routes