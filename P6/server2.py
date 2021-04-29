import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils

# Define the Server's port
PORT = 8080
list_sequences = ["TGACGATCGATCGACTG", "CGATCGATCGATCGATCGATCAGTC", "GACTCGATCGATCGATCGATCGATCG", "TATTAGCGGCTAGCTAGCTGATCCACAGTGCATG", "GCAGTCTGCTGCATGACTGACGTACTGCACAGTCAGTCAGT"]
list_genes = ["ADA", "U5", "FRAT1"]


BASES_INFORMATION = {
    "A":{"link": "https://es.wikipedia.org/wiki/Adenina",
        "formula": "C5H5N5",
        "name": "ADENINE",
         "colour": "green"

    },
    "C": {"link": "https://es.wikipedia.org/wiki/Citosina",
          "formula": "C4H5N3O",
          "name": "CYTOSINE",
            "colour": "blue"

          },
    "T": {"link": "https://es.wikipedia.org/wiki/Timina",
          "formula": "C5H6N2O2",
          "name": "Thymine",
        "colour": "red"

          },
    "G": {"link": "https://es.wikipedia.org/wiki/Guanina",
          "formula": "C5H5N5O",
          "name": "GUANINE",
            "colour": "pink"

          }
}

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

        file_name = self.path.strip("/")  # /info/A.html --> info/A.html
        context = {}
        if path_name == "/":
            context['n_sequences'] = len(list_sequences)
            context['list_genes'] = list_genes
            contents = server_utils.read_template_htm_file('./html/index.html').render(context=context)

        elif path_name == '/ping':
            contents = server_utils.read_template_htm_file('./html/ping.html').render()

        elif path_name == '/gene':
            gene = arguments['gene'][0]
            contents = server_utils.gene(gene)

        elif path_name == '/get':
            number_sequence = arguments['sequence'][0]
            contents = server_utils.get_seq(list_sequences, number_sequence)

        elif path_name.startswith('/operation'):
            sequence = arguments['sequence'][0]
            calculation = arguments['calculation'][0]

            if calculation == 'Info':
                try:
                    contents = server_utils.info_seq(sequence)
                except ZeroDivisionError:
                    error_msg = 'Incorrect sequence, please choose a valid one.'
                    context = {'sequence': sequence, 'result': error_msg, 'operation': 'Info'}
                    contents = server_utils.read_template_htm_file('./html/info.html').render(context=context)
            elif calculation == 'Comp':
                contents = server_utils.complement_seq(sequence)
            else:
                contents = server_utils.reversed_seq(sequence)

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