import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080
FOLDER = "./html/"

def read_html_file(filename):
    content = Path(filename).read_text()
    return content


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        file_name = self.path.strip("/")
        try:
            if file_name == "" or file_name == "index.html":
                contents = read_html_file(FOLDER + "index.html")
            else:
                contents = read_html_file(FOLDER + file_name)
        except FileNotFoundError:
            contents = read_html_file(FOLDER + "Error.html")


        # Generating the response message
        self.send_response(200)  # -- Status line: OK! # it means success

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished  # despues de los send_headers, luego el end_headers
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())  # igual que el send

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()