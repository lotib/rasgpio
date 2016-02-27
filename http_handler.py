import SimpleHTTPServer
import SocketServer
import json
import imp
from os import listdir
from os.path import isfile, join
import re
import inspect
import signal, os

PLUGIN_PATH="plugins"
PORT = 8000
plugins = {}


class RaspHttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

        def do_GET(self):
                print "get", self.path
                for key, plugin in plugins.iteritems():
                        print key
                        if self.path == '/' + key:
                                self.send(json.dumps(plugin.get_data(self.path)))
                                return
                
                if self.path == '/all':
                        print "all"
                        self.send(json.dumps([2,3]))
                else:
                        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
                        

	def send(self, response):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(response)
                

def load_plugins():

        plugin_files = [f for f in listdir(PLUGIN_PATH) if isfile("{}/{}".format(PLUGIN_PATH, f)) and f.endswith(".py")]
        print plugin_files
        
        for f in plugin_files:
                plugin_module = imp.load_source(PLUGIN_PATH, "{}/{}".format(PLUGIN_PATH, f))

                print plugin_module

                for name, obj in inspect.getmembers(plugin_module):
                
                        print obj
                        if inspect.isclass(obj):
                
                                plugin_obj = obj()
                                print 
                                plugins[plugin_obj.get_name()] = plugin_obj




def handler(signum, frame):

        for key, plugin in plugins.iteritems():
                del plugin
                
        print 'Signal handler called with signal', signum



signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

                                
load_plugins()

maled1 = led() 
        
SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("", PORT), RaspHttpHandler)
print "serving at port", PORT
httpd.serve_forever()

