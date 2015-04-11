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
