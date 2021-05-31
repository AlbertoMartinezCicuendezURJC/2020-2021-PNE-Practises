import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils


# Define the Server's port
PORT = 8080

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
        termcolor.cprint(self.path, "blue")
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        o = urlparse(self.path) # object
        path_name = o.path
        arguments = parse_qs(o.query)
        print('Resource requested: ', path_name)
        print('Parameters', arguments)

        context = {}
        if path_name == "/":
            contents = server_utils.read_template_htm_file('./html/index.html').render()

        elif path_name == '/karyotype':
            try:
                specie = arguments['specie'][0]
                contents = server_utils.print_karyotype(specie)
            except KeyError:
                contents = server_utils.read_template_htm_file('./html/Error.html').render()
            except UnicodeEncodeError:
                contents = server_utils.read_template_htm_file('./html/Error.html').render()

        elif path_name == '/chromosomeLength':
            if arguments == {} or len(arguments) == 1:
                contents = server_utils.read_template_htm_file('./html/Error.html').render()

            else:
                specie = arguments['specie'][0]
                chr_number = arguments['chromo'][0]
                contents = server_utils.print_chr_length(specie, chr_number)

        elif path_name == '/listSpecies':
            if arguments != {}:
                limit = arguments['limit'][0]


        else:
            contents = server_utils.read_template_htm_file('./html/Error.html').render()


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