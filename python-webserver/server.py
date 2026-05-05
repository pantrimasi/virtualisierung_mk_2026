#!/usr/bin/python3
# All imports
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading

# Yep, localhost
hostName = "0.0.0.0"
# HTTP Port for Webserver
serverPort = 8081


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # curl http://<ServerIP>/index.html
        if self.path == "/":
            # Respond with the file contents.
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = open("index.html", "rb").read()
            self.wfile.write(content)
        else:
            self.send_response(404)
        return


# Multithreaded Webserver
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == "__main__":
    webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
