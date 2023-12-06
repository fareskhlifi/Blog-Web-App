from flaskblog import app

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

