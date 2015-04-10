# from py2neo import neo4j
# from py2neo import node, rel, ogm
# #TODO: not sure I need an ogm
#
# from py2neo import cypher
# 
#
# graph_db = neo4j.GraphDatabaseService("http://localhost:7476/db/data/")
# store = ogm.Store(graph_db)
#
#
# ###============ Nodes and Relationship Creation ===============###
#
# def LoginOrRegister(email, password):
#   """ Description: If user exists, log in, if not, create new user.
#       Params: email and password from login form
#       Returns: user ID string """
#
#       teachers = graph_db.get_or_create_index(neo4j.Node, "Teachers")
#       possibleTeacher = teachers.get("email", email)
#       if possibleTeacher:
#         return possibleTeacher[0]._properties
