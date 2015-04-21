import config
from py2neo import Graph, Node, Relationship, watch, authenticate, rel
authenticate("localhost:7474", config.DATABASE_USER_NAME, config.DATABASE_PASSWORD)
graph = Graph()

#for debugging
watch("httpstream")


###=============== Nodes  Creation ==================###


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

  teacher_node = graph.cypher.execute("MATCH (n:Teacher) WHERE n.email ='"
                + email + "' AND n.password ='" + password + "'  RETURN n")
  teacher_name = teacher_node.records[0].n.properties["name"]
  if bool(teacher_node.records):
    print "OMG there is a node with that password and email!"
    return teacher_name
  print "Whoops, empty records. You do not exist"
  return False

def find_teacher_node(teacher):
  """ Description: Given a teacher's name, return the teacher node
      Params: teacher name (string)
      Returns: teacher node object if sucessful, otherwise false"""
  # teacher_node = graph.cypher.execute("MATCH (n:Teacher) WHERE n.name ='"
  #             + teacher + "' RETURN n")
  # teacher_name = teacher_node.records[0].n.properties["name"]
  #
  # teacher_node = Node("Teacher", name=teacher)
  # print (teacher_node, bool(teacher_node))
  # print dir(teacher_node)
  # print teacher_node.exists
  # teacher_node.bind("http://localhost:7474/db/data", metadata=None)
  # return teacher_node.properties.keys

  teacher_node = graph.find_one("Teacher", property_key="name", property_value=teacher)
  # teacher_node.bind("http://localhost:7474/db/data", metadata=None)
  # print ("teacher_node exists and is :", teacher_node)
  if bool(teacher_node):
    return teacher_node
  return False

def find_activity_node(activity):
  """ Description: Given a teacher's name, return the teacher node
      Params: teacher name (string)
      Returns: teacher node object if sucessful, otherwise false"""
  activity_node = graph.find_one("Activity", property_key="name", property_value=activity)
  # activity_node.bind("http://localhost:7474/db/data", metadata=None)
  # print ("activity_node exists and is :", activity_node)
  if bool(activity_node):
    return activity_node
  return False

def look_up_possible_settings(activity):
  #TODO: Build this
  """ Description: Given a specific activity, find all possible setting options.
      Params: A specific actvity by name (string)
      Returns: A dictionary object with all possible settings selections given
              a specific activity"""


def find_queued_activity_settings(teacher):
  #TODO: Build this
  """ Description: Given a teacher, find the queued up active activity settings
      Params: A specific teacher (string)
      Returns: A json object of configured settings for a given activity"""


###============ Relationship  Creation ===============###


def create_teacher_activity_rel(teacher, activity, settings, class_subject, active):
  """ Description:  Given a teacher and an activity, create a 'Teacher's Activity'
                    relationship storing all setting configurations, associated class
                    and active status
      Params: teacher (string), activity (name of activity- string),
                    settings (dictionary of selected settings), class_subject (string),
                    active (boolean)
      Returns: Boolean if created sucessfully or not"""

  #find activity node
  activity_node = find_activity_node(activity)
  print ("This is an activity name:", activity_node["name"])
  print ("This should be a fucking activity id: ", activity_node._id)
  #find teacher node
  teacher_node = find_teacher_node(teacher)
  print ("This should be a fucking teacher id: ", teacher_node._id)
  print ("This is a teacher's name", teacher_node["name"])
  print "Why isnt this printing????"



  #bind activity node
  teacher_configured_activity = Relationship(teacher_node, "CONFIGURED", activity_node,
                                              settings=settings, class_subject=class_subject,
                                              active=active)
  pants = graph.create_unique(teacher_configured_activity)

  # then add the properties , {"settings":settings, "class_subject":class_subject,"active":active} ),
  #the push

  # print (teacher_configured_activity.exists, "Configured??")
  if pants:
    print pants[0]
    return True
  return False


###============= Relationship  Access ================###
