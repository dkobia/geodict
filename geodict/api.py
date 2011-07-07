__author__ = "SwiftRiver Team"
__copyright__ = "Copyright 2011, Ushahidi Inc."
__credits__ = ["David Kobia"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "SwiftRiver Team"
__email__ = "swiftdev@ushahidi.com"
__status__ = "Development"

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import csv, os, os.path, sys, json, csv, resources
import geodict_lib, cliargs
import cProfile

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        text =  self.get_argument("text")
        locations = geodict_lib.find_locations_in_text(text)
        output_string = json.dumps(locations)
        self.write(output_string)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()