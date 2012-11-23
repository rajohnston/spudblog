import os
import webapp2
import django
from google.appengine.ext.webapp import template

from Models import *

class Home(webapp2.RequestHandler):
 def get(self):
  posts = db.GqlQuery("SELECT * FROM Posts ORDER BY datecreated DESC")
  base_template = "base.html"
  divider = self.request.get('divider')
  if divider:
   spud_divider = int(divider)
  else:
   spud_divider = 3
  template_values = {
    'posts' : posts,
    'base_template' : base_template,
    'spud_divider' : spud_divider,
   	}
  path = os.path.join(os.path.dirname(__file__), "../Views/html/home.html" )    
  self.response.out.write(template.render(path, template_values))   
  

class ViewPost(webapp2.RequestHandler):
 def get(self):
  base_template = "base.html"
  key = self.request.get('key')
  post = Posts.get(key)
  template_values = {
    'base_template' : base_template,
    'post' : post,
   	}
  path = os.path.join(os.path.dirname(__file__), "../Views/html/viewpost.html" )    
  self.response.out.write(template.render(path, template_values))   

      
class AddorEdit(webapp2.RequestHandler):
 def get(self):
  base_template = "base.html"
  key = self.request.get('key')
  add_or_edit = "add"
  post=""
  if key:
   add_or_edit = "edit"
   post = Posts.get(key)
  template_values = {
    'base_template' : base_template,
    'post' : post,
    'add_or_edit' : add_or_edit,
   	}
  path = os.path.join(os.path.dirname(__file__), "../Views/html/edit.html" )    
  self.response.out.write(template.render(path, template_values))   

      
 def add(self):
  post = Posts()
  post.title = self.request.get('title')
  post.text = self.request.get('text')
  post.put()
  self.redirect('/')
 
 
 def edit(self):
  key = self.request.get('key')
  post = Posts.get(key)
  post.title = self.request.get('title')
  post.text = self.request.get('text')
  post.put()
  self.redirect('/')


 def post(self):
  add_or_edit = self.request.get('add_or_edit')
  if add_or_edit == "add":
   self.add()
  else:
   self.edit() 



app = webapp2.WSGIApplication([
	('/',Home),
	('/viewpost',ViewPost),
	('/edit',AddorEdit),
	('/add',AddorEdit)],debug=True)
