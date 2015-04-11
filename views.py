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
  #TODO: add validation and login functionality
  #TODO: redirect to post teacher dashboard
  return render_template("login.html")

@app.route('/register')
def register_template():
  return render_template("registration.html")

@app.route('/register', methods=["POST"])
def register():
  #TODO: add error handling and validation
  form = request.form

  _name = form["name"]
  _email = form["email"]
  _password = form["password"]
  _school = form["school"]
  _class_subject = form["class_subject"]

  model.register_teacher(_name, _email, _password, _school, _class_subject)

  flash("Sucessfully Registered, please log in with credentials now")
  return redirect(url_for('login_template'))

# @app.route('/login', methods=["POST"])
# def authenticate():
#   form = forms.LoginForm(request.form)
#   if not form.validate():
#     flash("Email or Password incorrect")
#     return render_template("login.html")
#
#   email = form.email.data
#   password = form.password.data
#
#   user = User.query.filter_by(email=email).first()
#
#   if not user or no user.authenticate(password):
#     flash("Email or Password incorrect")
#     return render_template("login.html")
#
#   login_user(user)
#   return redirect(request.args.get("next", url_for("index")))


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
  app.run(debug=True)
