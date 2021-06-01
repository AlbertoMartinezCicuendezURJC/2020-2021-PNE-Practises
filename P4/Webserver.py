import socket
from pathlib import Path
import termcolor

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080
HTML_ASSEST = './html/'

def read_html_file(filename):
    content = Path(filename).read_text()
    return content

def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')
    req_line = lines[0]
    path_name = req_line.split(' ')[1]

    if path_name == "/":
        body = read_html_file(HTML_ASSEST + "index.html")
    elif "/info/" in path_name:
        try:
            base = path_name.split("/")[-1]
            body = read_html_file(HTML_ASSEST + base + '.html')
        except FileNotFoundError:
            body = read_html_file(HTML_ASSEST + 'Error.html')

    else:
        body = read_html_file(HTML_ASSEST + 'Error.html')



    """if path_name == '/':
        body = read_html_file(HTML_ASSEST + 'index.html')
    elif path_name == "/info/A":
        body = read_html_file(HTML_ASSEST + "A.html")
    elif path_name == "/info/C":
        body = read_html_file(HTML_ASSEST + "C.html")
    elif path_name == "/info/G":
        body = read_html_file(HTML_ASSEST + "G.html")
    else:
        body = read_html_file(HTML_ASSEST + "T.html")"""



    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n" #si pones plain en vez de html te dara el codigo tal cual

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()