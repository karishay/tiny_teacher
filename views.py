from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask.ext.login import LoginManager, login_required, login_user, current_user

import os
import config
import forms
import model

app = Flask(__name__)
app.config.from_object(config)


###========= Teacher Interface =========###

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/login')
def login_template():
  return render_template("login.html")

@app.route('/login', methods=["POST"])
def login():
  #TODO: add validation 
  form = request.form
  email = form["email"]
  password = form["password"]

  login = model.authenticate(email, password)
  if login:
    return redirect(url_for("dashboard"))
  flash("Password and Email invalid. Sucks to be you.")
  return render_template("login.html")

@app.route('/register')
def register_template():
  return render_template("registration.html")

@app.route('/register', methods=["POST"])
def register():
  #TODO: add error handling and validation
  form = request.form

  name = form["name"]
  email = form["email"]
  password = form["password"]
  school = form["school"]
  class_subject = form["class_subject"]

  model.register_teacher(name, email, password, school, class_subject)

  flash("Sucessfully Registered, please log in with credentials now")
  return redirect(url_for('login_template'))

@app.route('/dashboard')
def dashboard():
  return "logged in yay"

###=========== API endpoints ===========###


@app.route('/teachers')
def teachers_json():
  return render_template("teachers.json")

@app.route('/activity')
def activity_json():
  return render_template("activity.json")


###=====================================###
###=====================================###



if __name__ == "__main__":
  app.run(debug=True, port=5050)
