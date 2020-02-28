from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import pkg_parser as parser

# Ip and port configuration
hostName = "https://pure-caverns-80343.herokuapp.com/"
hostPort = 8080

# Path to a file
# Works only in Ubuntu or Debian
# filePath = "/var/lib/dpkg/status"

# A mock file
filePath = "/status.real"

# Iterates through the given list and 
# saves name of the package to another
# list
# Returns the list
def get_package_names(package_list):
    names = []

    for package in package_list:
        names.append(package["name"])

    return names

# Iterates through the given list and
# compares given name to the names of
# the packages in the list
# If it founds a match it returns the 
# found package
def get_package_by_name(name, package_list):

    package = {}

    for pkg in package_list:
        if pkg["name"] == name:
            package = pkg
            break

    return package

# Creates list of packages using package parser
# Initializes MyHttpServer class
# Start listening the given port
def main():

    package_list = parser.parse(filePath)

    class MyHttpServer(BaseHTTPRequestHandler):

        # Receives all GET requests
        def do_GET(self):

            # If path is '/packages'
            # Sets content type to 'application/json'
            # Creates json array from all
            # the package names in the list
            # Sends the json array to a client
            if self.path == "/packages":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                package_names = get_package_names(package_list)
                package_names.sort()
                data = json.dumps(package_names)
                self.wfile.write(data.encode("utf-8"))

            # If path starts with '/packages/'
            # Sets content type to 'application/json'
            # Parses name of the package from the path
            # Loads package dictionary using the name
            # Creates json object of the package dictionary
            # Sends the json object to a client
            elif self.path.startswith("/packages/"):
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                package_name = self.path.replace("/packages/", "")
                package = get_package_by_name(package_name, package_list)
                data = json.dumps(package)

                self.wfile.write(data.encode("utf-8"))

            # If path is '/vue.js'
            # Sets content type to 'text/javascript'
            # Reads contents of the 'vue.js' file
            # Sends file contents to a client using
            # encoding 'utf-8'
            elif self.path == "/vue.js":
                self.send_response(200)
                self.send_header("Content-Type", "text/javascript")
                self.end_headers()

                f = open("vue.js", "r")
                self.wfile.write(f.read().encode("utf-8"))

            # If path is '/handler.js'
            # Sets content type to 'text/javascript'
            # Reads contents of the 'handler.js' file
            # Sends file contents to a client using
            # encoding 'utf-8'
            elif self.path == "/handler.js":
                self.send_response(200)
                self.send_header("Content-Type", "text/javascript")
                self.end_headers()

                f = open("handler.js", "r")
                self.wfile.write(f.read().encode("utf-8"))

            # If path is '/index.css'
            # Sets content type to 'text/css'
            # Reads contents of the 'index.css' file
            # Sends file contents to a client using
            # encoding 'utf-8'
            elif self.path == "/index.css":
                self.send_response(200)
                self.send_header("Content-Type", "text/css")
                self.end_headers()

                f = open("index.css", "r")
                self.wfile.write(f.read().encode("utf-8"))

            # If path is '/'
            # Sets content type to 'text/html'
            # Reads contents of the 'index.html' file
            # Sends file contents to a client using
            # encoding 'utf-8'
            elif self.path == "/":
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

if __name__ == "__main__":
    main()