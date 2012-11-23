
import os

from google.appengine.dist import use_library
use_library('django', '1.2')

import wsgiref.handlers
import webapp2


def main():
  app = webapp2.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
