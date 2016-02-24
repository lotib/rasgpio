import SimpleHTTPServer
import SocketServer
import json

PORT = 8000

class RaspHttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

        def do_GET(self):
                
                print "get", self.path

                if self.path == '/all':
                        print "all"
                        self.send(json.dumps([2,3]))
                else:
                        print "else"
                        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

                print "end"
                        

	def send(self, response):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(response)
                
			
Handler = RaspHttpHandler

SocketServer.TCPServer.allow_reuse_address = True
#server = SocketServer.TCPServer((host, port), MyServer)

httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT

httpd.serve_forever()

