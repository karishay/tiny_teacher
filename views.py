from flask import Flask, render_template
from flask.ext.login import LoginManager, login_required, login_user, current_user

#import config
import forms
import model

app = Flask(__name__)
#app.config.from_object(config)

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
def login():
  return render_template("login.html")

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
  app.run()
