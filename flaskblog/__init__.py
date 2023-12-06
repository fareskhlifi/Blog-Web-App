from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '8ee4f8a77ded46b31fbfb044a3068889'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # redirect you to the login function interface when you try to access account from the url without logging in first 
login_manager.login_message_category = 'info' # personalize the message shown automatically

from flaskblog import routes



# generate a secret_key to protect the app against modifying cookies, attacks, etc
# import secrets
# secrets.token_hex(16)

# generating a password hash with Bcrypt, a different hash is generated every time
#  from flask_bcrypt import Bcrypt
# >>> bcrypt = Bcrypt()
# >>> bcrypt.generate_password_hash('testing') 
# >>> bcrypt.generate_password_hash('testing').decode('utf-8') -> return a regular string
# >>> hashed = bcrypt.generate_password_hash('testing').decode('utf-8') 
# >>> bcrypt.check_password_hash(hashed, 'testing')  -> True
