from flask import Flask, render_template
app = Flask(__name__)

###========= Teacher Interface =========###

@app.route('/')
def index():
  return render_template("index.html")


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
