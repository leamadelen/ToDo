from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
import os

#UPLOAD_FOLDER = './backend/profilepics'  # Update this path as needed
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, 'profilepics')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from .models import User, Todo, Category
from .routes import auth, profile, todos, categories

with app.app_context():
    # Create database tables
    db.create_all()
