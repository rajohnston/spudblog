import os
import webapp2
import django
from Models import *

class Home(webapp2.RequestHandler):
 def get(self):
  self.response.out.write("Home")  

class Add(webapp2.RequestHandler):
 def get(self):
  self.response.out.write("Add")  


app = webapp2.WSGIApplication([
	('/',Home),
	('/add',Add)],debug=True)
