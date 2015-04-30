from flask import Flask, render_template, request, session, flash, redirect, url_for, json, jsonify
from flask.ext.login import LoginManager, login_required, login_user, current_user

import os
import config
import forms
import model

app = Flask(__name__)
app.config.from_object(config)

###=====================================###
###========= Teacher Interface =========###
###=====================================###

###= Login and Registration ============###


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

  name = model.authenticate(email, password)
  if name:
    return render_template("dashboard.html", name=name)
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
  return render_template("dashboard.html")


###= Activity Manipulation ============###


@app.route('/activity_settings', methods=["GET"])
def activity_settings():
  activities={"Phone Push":
        ("phone_push","Ever wanted to push your phone? There's an app for that!"), "Nic is Awesome":
        ("nic_is_awesome","This activity proves scientifically the objective awesomeness that is Nic"),
        "Operation Badass": ("operation_badass",
        "If I told you the description of this activity I'd have to kill you.")}
  return render_template("activity_settings.html", activities=activities)

@app.route('/<activity>')
def render_activity_settings(activity):
  #activity_specific_settings = Model.look_up_possible_settings(activity)
  #return render_template("activity.html", activity_settings=activity_specific_settings)
  return "Yay, activity is %s" % activity


@app.route('/test/')
def test():
  ###------=============================================-------###
  ######## testing look up possible settings by activity #########
  ###------=============================================-------###
  #TODO: Have Nic test if this needs to be unwrapped and rewrapped
  activity = "DecayDice"
  settings = model.look_up_possible_settings(activity)

  if settings:
    print "Ohai I am trying to load Json, Did it work?"
    return settings
  return "No active configured activites right now :("

@app.route('/test_configure/')
def test_configure():
  ###------=============================================-------###
  ######### testing creation of Configured Relationships #########
  ###------=============================================-------###
  teacher = "Shannon Burns"
  activity = "DecayDice"
  settings = {
      "teacher_name" : "Shannon Burns",
      "activity_name": "DecayDice",
      "preset": ["a","b","c"],
      "selected_settings": {
          "preset": ["a","b","c"],
          "display_data": {
              "initial_velocity": "true",
              "time": "true",
              "distance": "false",
              "deceleration": "false"
          },
          "table_data": {
              "initial_velocity": "true",
              "time": "false",
              "distance": "true",
              "deceleration": "false"
          },
          "include_blank_columns": "false",
          "display_best_fit": "false"
        }
  }

  settings_string = json.dumps(settings)

  print ("This is settings:", settings_string)
    #Settings will be gotten from the form
  class_subject = ["Physics", "Spring 2015"]
  active = True
  relationship = model.create_teacher_activity_rel(teacher, activity, settings_string, class_subject, active)
  if relationship:
    return ("The relationship was created: ", relationship)
  return ("relationship was not created :(")

@app.route('/test_queued_activities')
def test_queued_activities():
  teacher = "Shannon Burns"
  queued_activity = model.find_queued_activity_settings(teacher)
  return queued_activity

@app.route('/display_settings_options')
def display_settings_options():
  question_group = [
      {"Forget-Me-Now":{"description": "Say goodbye to these because it's the last time! That's why you always leave a note! I've opened a door here that I regret. Marry me. He'll want to use your yacht, and I don't want this thing smelling like fish. I care deeply for nature.","time": 3, "materials": None}},
      {"Top Banana":{"description" : "A flower in my garden, a mystery in my panties. There are dozens of us! Dozens! If mother sees this, she will blow a cow. No, no, it's pronounced a-nal-ra-pist. It wasn't really the pronunciation that bothered me.", "time": 2, "materials": "banana"}},
      {"NO TOUCHING!":{"description" : "We need a name. Maybe 'Operation Hot Mother.'' No, let's try to top that. (They never did.) Please refrain from Mayoneggs during this salmonella scare.", "time": 2, "materials": None}}
  ]

  return render_template("display_possible_settings.html", questions=question_group)

@app.route('/student_results')
def student_results():
  return "This is where you can see student's results"


###=====================================###
###=========== API endpoints ===========###
###=====================================###



@app.route('/teachers')
def teachers_json():
  return render_template("teachers.json")

@app.route('/teachers/<teacher>')
def activity_json(teacher):
  #TODO: call model.find_teacher(teacher) to return active settings
  #for queued activity for the teacher
  if teacher == "Nic Harrigan":
    return render_template("activity.json")
  if teacher == "Shannon Burns":
    return render_template("decay_dice.json")
  return "{'Sorry, that teacher doesn't have any activities queued up'}"


###=====================================###
###===========Admin Interface===========###
###=====================================###


#TODO: limit access to admins and add admin login

@app.route('/create_activity', methods=["GET"])
def create_activity_template():
  return render_template("create_activity.html")

@app.route('/create_activity', methods=["POST"])
def create_activity():
  #TODO: check validity
  form = request.form
  name = form["activity_name"]
  settings = form["settings"]
  presets = "Presets will be dealt with later, when we care more."
  preview = form["preview"]

  new_activity = model.create_activity(name, settings, presets, preview)
  if new_activity:
    flash("Sucessfully created new activity, now log in as a teacher to set it up!")
    return redirect(url_for("login_template"))
  flash("Activity was not created sucessfully, double check your JSON and try again!")
  return redirect(url_for("create_activity"))




###=====================================###
###=====================================###



if __name__ == "__main__":
  app.run(debug=True, port=5050)
