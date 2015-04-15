import config
from py2neo import Graph, Node, Relationship, watch, authenticate
authenticate("localhost:7474", config.DATABASE_USER_NAME, config.DATABASE_PASSWORD)
graph = Graph()

#for debugging
watch("httpstream")


###============ Nodes and Relationship Creation ===============###


def register_teacher(name, email, password, school, class_subject):
  """ Description: for new teacher, create new teacher node
      Params: name, email, password, school, class_subject from registration forms
      Returns: true if correctly added to graph"""
  new_teacher = Node("Teacher", name=name,
                      email=email,
                      password=password,
                      school=school,
                      class_subject=class_subject)
  graph.create(new_teacher)
  return new_teacher.exists

def create_activity(activity_name, settings, setting_presets, preview):
  """ Description: Creates a new activity node
      Params: Activity Name (string), Settings (dictionary), Setting Presets (dict of dicts),
              Preview: (url to resource)
      Returns: true if correctly added to graph"""
  new_activity = Node("Activity", name=activity_name,
                      settings=settings,
                      preset=setting_presets,
                      preview=preview)
  graph.create(new_activity)
  return new_activity.exists

  
###============ Nodes and Relationship Access ===============###

def authenticate(email, password):
  """ Description: Validates and authenticates email and password combinations
                   by checking against database
      Params: Email and Password from form
      Returns: boolean """

  teacher_node = graph.cypher.execute("MATCH (n:Teacher) WHERE n.email ='" + email + "' AND n.password ='" + password + "'  RETURN n")
  teacher_name = teacher_node.records[0].n.properties["name"]
  if teacher_node.records:
    print "OMG there is a node with that password and email!"
    return teacher_name
  print "Whoops, empty records. You do not exist"
  return False

def look_up_possible_settings(activity):
  """ Description: Given a specific activity, find all possible setting options.
      Params: A specific actvity by name (string)
      Returns: A dictionary object with all possible settings selections given a specific activity"""
