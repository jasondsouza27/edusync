from flask import Flask, render_template, url_for, flash, redirect
from signup import LoginForm, SignupForm
#from flask_sqlalchemy import SQLAlChemy

app= Flask(__name__)
app.config['SECRET_KEY'] = '738d92b038d702d2b3df4455ed26dfd2'
'''app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlChemy(app)

class User(db.Model):
    pid=db.Coloumn(db.Integer, primary_key=True)
    name=db.Coloumn(db.String(20), nullable=False)
    email=db.Coloumn(db.String(120),unique=True, nullable=False)
    image=db.Coloumn(db.String(20), nullable=False)
    password=db.Coloumn(db.String(60),nullable=False)

    def __repr__(self):
        return f"User ({self.name}, {self.email},{self.image})"'''


@app.route("/")
def home():
    return "test"

@app.route("/signup",methods=['POST','GET'])
def signup():
    form= SignupForm()
    if form.validate_on_submit():
        flash("Account created",'success')
        return redirect(url_for('home'))
    return render_template('signup.html',form=form)
    
@app.route("/login" ,methods=['POST','GET'])
def login():
     form= LoginForm()
     if form.validate_on_submit():
        flash("Account created",'success')
        return redirect(url_for('home'))
     return render_template('login.html',form=form)

if '__name__'=='__main__':
    app.run(debug=True)
