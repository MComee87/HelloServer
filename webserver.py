from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                try:
                        if self.path.endswith("/hello"):
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()

                                output = ""
                                output += "<html><body><p style='color:blue; background-color:purple; margin-right:auto; margin-left:auto; font-size:72px; font-family: 'cursive;'>Hello!</p> <a href = '/index'>Back to home</a></body></html>"
                                self.wfile.write(output)
                                print output
                                return

                        if self.path.endswith("/hola"):
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()

                                output = ""
                                output += "<html><body><p style='color:purple; background-color:blue; margin-right:auto; margin-left:auto; font-size:72px; font-family: 'cursive;'>&#161Hola!</p> <a href = '/index'>Back to home</a></body></html>"
                                self.wfile.write(output)
                                print output
                                return

                        if self.path.endswith("/index"):
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.end_headers()

                                output = ""
                                output += "<html><body><p style='color:white; margin-right:auto; margin-left:auto; font-size:72px; font-family:'cursive;'><a style = 'background-color:blue; color:white;' href = '/hello'>Hello</a> <a style = 'background-color:green; color:white;' href = '/hola'>&#161Hola!</a></p></body></html>"
                                self.wfile.write(output)
                                print output
                                return

                        

                except IOError:
                        self.send_error(404, "File Not Found %s" % self.path)


def main():
        try:
                port = 8080 
                server = HTTPServer(('',port), webserverHandler)
                print "Web server running on port %s" % port
                server.serve_forever()

        except KeyboardInterrupt:
                print "^C entered, stopping web server..."
                server.socket.close()


if __name__ == '__main__':
        main()
