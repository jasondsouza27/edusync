from flask import render_template, url_for, flash, redirect, request
from EduSync_git import app, db, bcrypt
from EduSync_git.signup  import SignupForm, LoginForm
from EduSync_git.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home():
    return "test"


@app.route("/signup",methods=['POST','GET'])
def signup():
    form= SignupForm()
    if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(name=form.name.data,email=form.email.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Account created",'success')
        return redirect(url_for('login'))
    return render_template('signup.html',form=form)
    
@app.route("/login" ,methods=['POST','GET'])
def login():
     form= LoginForm()
     if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            return  redirect(url_for('home'))
        else:
            flash("Account created",'success')
     return render_template('login.html',form=form)