import os
import datetime
from google.appengine.ext import db

class Posts(db.Model):
 datecreated = db.DateTimeProperty(auto_now_add=True)
 datemodified = db.DateTimeProperty(auto_now=True)
 title = db.StringProperty()
 text = db.TextProperty()
