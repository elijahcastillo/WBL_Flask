from flask import Flask
from flask_sqlalchemy import SQLAlchemy





#database instance
db = SQLAlchemy()

# Uncomment to create database
# with app.app_context():
#     db.create_all()

def create_app():
    #app instance
    app = Flask(__name__)

    #Config
    app.config["SECRET_KEY"] = "71WU6W2qf4srJSmxrl54ua1onxQHSMbF"  #For more security, use .env file
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    
    db.init_app(app)
    
    #Blueprints
    from src.routes.main import routes
    app.register_blueprint(routes)
    
    return app