import re
import os
import datetime
import string
import math
import logging

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import blobstore

class Users(db.Model): #this is the User database used to associate security
 email = db.EmailProperty()
 datecreated = db.DateTimeProperty(auto_now_add=True)
 datemodified = db.DateTimeProperty(auto_now=True)
 usertype = db.StringProperty()
