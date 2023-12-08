from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail 
from flaskblog.config import Config



db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' # redirect you to the login function interface when you try to access account from the url without logging in first 
login_manager.login_message_category = 'info' # personalize the message shown automatically
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app



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
