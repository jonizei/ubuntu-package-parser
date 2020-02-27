from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import pkg_parser as parser

hostName = "localhost"
hostPort = 8080
filePath = "/var/lib/dpkg/status"

def main():

    package_list = parser.parse(filePath)

    class MyHttpServer(BaseHTTPRequestHandler):

        def do_GET(self):

            if self.path == "/packages":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                data = json.dumps(package_list)
                self.wfile.write(data.encode("utf-8"))

            elif self.path == "/jquery-3.4.1.min.js":
                self.send_response(200)
                self.send_header("Content-Type", "text/javascript")
                self.end_headers()

                f = open("jquery-3.4.1.min.js", "r")
                self.wfile.write(f.read().encode("utf-8"))

            elif self.path == "/index.css":
                self.send_response(200)
                self.send_header("Content-Type", "text/css")
                self.end_headers()

                f = open("index.css", "r")
                self.wfile.write(f.read().encode("utf-8"))

            else:
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()

                f = open("index.html", "r")
                self.wfile.write(f.read().encode("utf-8"))

    myhttpserver = HTTPServer((hostName, hostPort), MyHttpServer)
    print("Listening", hostPort)

    try:
        myhttpserver.serve_forever()
    except KeyboardInterrupt:
        pass

    myhttpserver.server_close()
    print("Stopped listening", hostPort)

main()