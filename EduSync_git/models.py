from datetime import datetime
from EduSync_git import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    pid=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)
    image=db.Column(db.String(20), nullable=True,default="default_image.jpg")
    password=db.Column(db.String(60),nullable=False)


    def get_id(self):
        return str(self.pid)

    def __repr__(self):
        return f"User ({self.name}, {self.email},{self.image})"