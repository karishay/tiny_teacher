from flask import Flask, render_template, request
from flask.ext.login import LoginManager, login_required, login_user, current_user

import config
import forms
import model

app = Flask(__name__)
app.config.from_object(config)

###============= Login ==============###

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"
#
# @login_manager.user_loader
# def load_user(user_id):
#   #if this queries User table, wont it be Model.user?
#   return User.query.get(user_id)

###=====================================###
###=====================================###


###========= Teacher Interface =========###

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/login')
def login_template():
  return render_template("login.html")

@app.route('/register')
def register_template():
  return render_template("registration.html")

@app.route('/register', methods=["POST"])
def register():
  #get the values from the forms
  form = request.form

  f = request.form
  for key in f.keys():
      for value in f.getlist(key):
          print key,":",value


  _name = form["name"]
  _email = form["email"]
  _password = form["password"]
  _school = form["school"]
  _class_subject = form["class_subject"]

  #build the node
  model.register_teacher(_name, _email, _password, _school, _class_subject)

  #return login page
  return render_template('login.html')

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
