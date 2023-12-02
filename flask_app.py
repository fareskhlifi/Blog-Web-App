from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# generate a secret_key to protect the app against modifying cookies, attacks, etc
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '8ee4f8a77ded46b31fbfb044a3068889'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')" 


posts = [
    {
        'author': 'Fares Khelifi',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'November 30, 2023'
    },
    {
        'author': 'Amine Khelifi',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'November 30, 2023'
    }
]



@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful, Please check Username and Password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)




# set up the database
# from flask_app import app, db
# app.app_context().push()
# db.create_all()

# create users in db
# from flask_app import User, Post
# with app.app_context():
#   user_1 = User(username='fares', email='fares@gmail.com', password='password')
#   db.session.add(user_1)
#   db.session.commit()

# get the created users
# with app.app_context:
#   User.query.all()

# other commands: user.query.filter_by(username='example').all()
# first user: User.query.first()
# User.query.get(1) -> get the user with id = 1

