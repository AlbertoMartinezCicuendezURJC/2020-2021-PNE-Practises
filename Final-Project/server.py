import http.server
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils
from ensembl_class import Ensembl
import json

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        o = urlparse(self.path) # object
        path_name = o.path
        arguments = parse_qs(o.query)
        print('Resource requested: ', path_name)
        print('Parameters', arguments)

        if path_name == "/":
            contents = server_utils.read_template_htm_file('./html/index.html').render()
            content_type = 'text/html'

        elif path_name == '/karyotype':
            try:
                if 'json' in arguments.keys() and arguments['json'][0] == '1' and len(arguments) == 2:
                    specie = arguments['specie'][0]
                    param_json = True
                    contents = server_utils.print_karyotype(specie, param_json)
                    contents = json.dumps(contents)
                    content_type = 'application/json'

                else:
                    if arguments == {} or (len(arguments) == 1 and 'json' in arguments.keys()):
                        contents = server_utils.read_template_htm_file('html/Error_blank.html').render()
                        content_type = 'text/html'
                    else:
                        specie = arguments['specie'][0]
                        param_json = False
                        contents = server_utils.print_karyotype(specie, param_json)
                        content_type = 'text/html'

            except KeyError:
                contents = server_utils.read_template_htm_file('./html/Error.html').render()
            except UnicodeEncodeError:
                contents = server_utils.read_template_htm_file('./html/Error.html').render()

        elif path_name == '/chromosomeLength':
            if 'json' in arguments.keys() and arguments['json'][0] == '1' and len(arguments) == 3:
                param_json = True
                specie = arguments['specie'][0]
                chr_number = arguments['chromo'][0]
                contents = server_utils.print_chr_length(specie, chr_number, param_json)
                contents = json.dumps(contents)
                content_type = 'application/json'

            else:
                if arguments == {} or len(arguments) == 1 or (len(arguments) == 2 and 'json' in arguments.keys()):
                    contents = server_utils.read_template_htm_file('./html/Error_blank.html').render()
                    content_type = 'text/html'

                else:
                    specie = arguments['specie'][0]
                    chr_number = arguments['chromo'][0]
                    param_json = False
                    contents = server_utils.print_chr_length(specie, chr_number, param_json)
                    content_type = 'text/html'

        elif path_name == '/listSpecies':
            if 'json' in arguments.keys() and arguments['json'][0] == '1' and len(arguments) == 2:
                limit = arguments['limit'][0]
                param_json = True
                contents = server_utils.print_limit(limit, param_json)
                contents = json.dumps(contents)
                content_type = 'application/json'

            else:
                if arguments == {} or (len(arguments) == 1 and 'json' in arguments.keys()):
                    limit = Ensembl.counter_species()

                    if 'json' in arguments.keys():
                        param_json = True
                        contents = server_utils.print_limit(limit, param_json)
                        contents = json.dumps(contents)
                        content_type = 'application/json'

                    else:
                        param_json = False
                        contents = server_utils.print_limit(limit, param_json)
                        content_type = 'text/html'


                else:
                    limit = arguments['limit'][0]
                    param_json = False
                    contents = server_utils.print_limit(limit, param_json)
                    content_type = 'text/html'

        elif path_name == '/geneSeq':
            if 'json' in arguments.keys() and arguments['json'][0] == '1' and len(arguments) == 2:
                gene = arguments['gene'][0]
                param_json = True
                contents = server_utils.print_sequence(gene, param_json)
                contents = json.dumps(contents)
                content_type = 'application/json'

            else:
                if arguments == {} or (len(arguments) == 1 and 'json' in arguments.keys()):
                    contents = server_utils.read_template_htm_file('html/Error_blank.html').render()
                    content_type = 'text/html'

                else:
                    gene = arguments['gene'][0]
                    param_json = False
                    contents = server_utils.print_sequence(gene, param_json)
                    content_type = 'text/html'

        elif path_name == '/geneInfo':
            if 'json' in arguments.keys() and arguments['json'][0] == '1' and len(arguments) == 2:
                gene = arguments['gene'][0]
                param_json = True
                contents = server_utils.print_info(gene, param_json)
                contents = json.dumps(contents)
                content_type = 'application/json'

            else:
                if arguments == {} or (len(arguments) == 1 and 'json' in arguments.keys()):
                    contents = server_utils.read_template_htm_file('html/Error_blank.html').render()
                    content_type = 'text/html'

                else:
                    gene = arguments['gene'][0]
                    param_json = False
                    contents = server_utils.print_info(gene, param_json)
                    content_type = 'text/html'

        elif path_name == '/geneCalc':
            if 'json' in arguments.keys() and arguments['json'][0] == '1' and len(arguments) == 2:
                gene = arguments['gene'][0]
                param_json = True
                contents = server_utils.print_calc(gene, param_json)
                contents = json.dumps(contents)
                content_type = 'application/json'

            else:
                if arguments == {} or (len(arguments) == 1 and 'json' in arguments.keys()):
                    contents = server_utils.read_template_htm_file('html/Error_blank.html').render()
                    content_type = 'text/html'

                else:
                    gene = arguments['gene'][0]
                    param_json = False
                    contents = server_utils.print_calc(gene, param_json)
                    content_type = 'text/html'

        else:
            contents = server_utils.read_template_htm_file('./html/Error.html').render()
            content_type = 'text/html'


        # Generating the response message
        self.send_response(200)  # -- Status line: OK! # it means success

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
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