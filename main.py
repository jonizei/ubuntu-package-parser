from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import pkg_parser as parser

hostName = "localhost"
hostPort = 8080
filePath = "/var/lib/dpkg/status"

def get_package_names(package_list):
    names = []

    for package in package_list:
        names.append(package["name"])

    return names

def get_package_by_name(name, package_list):

    package = {}

    for pkg in package_list:
        if pkg["name"] == name:
            package = pkg
            break

    return package

def main():

    package_list = parser.parse(filePath)

    class MyHttpServer(BaseHTTPRequestHandler):

        def do_GET(self):

            if self.path == "/packages":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                data = json.dumps(get_package_names(package_list))
                self.wfile.write(data.encode("utf-8"))

            elif self.path.startswith("/packages/"):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                package_name = self.path.replace("/packages/", "")
                package = get_package_by_name(package_name, package_list)
                data = json.dumps(package)

                self.wfile.write(data.encode("utf-8"))

            elif self.path == "/vue.js":
                self.send_response(200)
                self.send_header("Content-Type", "text/javascript")
                self.end_headers()

                f = open("vue.js", "r")
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