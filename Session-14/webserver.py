import http.server
import socketserver  # socket module itself is imported from socketserver

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# -- Use the http.server Handler
Handler = http.server.SimpleHTTPRequestHandler  # used by TCP server, it listens to an ip and a port, if a client connects, TCP dice, tengo una request pero no se managearlo, pero el handler lo hace asi que se la paso al handler (entiende el mensaje HTTP)
# las "" de la tupla es que escucha a todas las ips que tienes en tu ordenador
# -- Open the socket server
# el socketserver es la conexion para pasar el mensaje del TCP al handler
with socketserver.TCPServer(("", PORT), Handler) as httpd:  # el primer elemento de la tupla es la ip (puede ser localhost, una en especifico...)

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server Stopped!")
        httpd.server_close()