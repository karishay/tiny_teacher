from flask import Flask, render_template
app = Flask(__name__)

@app.route('/teachers')
def teachers_json():
  return render_template("teachers.json")

@app.route('/activity')
def activity_json():
  return render_template("activity.json")

if __name__ == "__main__":
  app.run()
