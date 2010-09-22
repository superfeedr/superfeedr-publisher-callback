#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from urlparse import urlparse

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('')

    def post(self):
        # Logging all arguments
        # You can commeny out these lines.
        for param in self.request.arguments() :
           logging.info(param + " = " + self.request.get(param))
        
        # You should define the rules here. For example, you can list authroized callbacks
        # Or maybe ask for another param (like an API key, that you can then compare to your list of API keys)
        if self.request.get("apikey") == "12345" :
          self.response.set_status(204)
        else :
          self.response.set_status(401)
          self.response.out.write("Please submit your API key as an 'apikey' param.")

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
