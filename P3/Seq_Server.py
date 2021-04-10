import socket
import server_utils


list_sequences = ["AGCTAGCTACT", "ATGCATCGATGCATGCTGACTGACTATGCTAG", "ATGCATGCATGCAGCT", "AGCTATAGCTAGCTACTG"]
PORT = 8080
IP = "127.0.0.1"
c_counter = 0
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
client_address_list = []

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()
    client_address_list.append(client_ip_port)
    c_counter += 1
    print("CONNECTION: " + str(c_counter) + " CLient IP, PORT: " + str(client_ip_port))
    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    formatted_message = server_utils.format_command(msg)
    formatted_message = formatted_message.split(" ")

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]

    if formatted_message == "PING":
        server_utils.ping()
        response = "OK!"
        cs.send(response.encode())
    elif command == "GET":
        try:
            response = list_sequences[int(argument)]
            cs.send(response.encode())
        except Exception:
            response = "The choosen index is out of the range. Please, choose an integer number between 0 and 3"
            cs.send(response.encode())

    elif command == "INFO":
        try:
            response = server_utils.print_info(argument)
            cs.send(response.encode())
        except ZeroDivisionError:
            response = "Invalid sequence. Please, choose a correct one."
            cs.send(response.encode())

    elif command == "COMP":
            response = server_utils.complement_seq(argument)
            cs.send(response.encode())

    elif command == "REV":
            response = server_utils.reversed_seq(argument)
            cs.send(response.encode())

    elif command == "GENE":
        try:
            response = server_utils.read_sequence(argument)
            cs.send(response.encode())
        except FileNotFoundError:
            response = "The requested folder has not be founded. Please, you another one."
            cs.send(response.encode())
        except PermissionError:
            response = "Please, choose a gene in order to read it."
            cs.send(response.encode())
        except OSError:
            response = "Invalid argument. Please, choose a valid gene name."
            cs.send(response.encode())

    else:
        response = "Not available command"
        cs.send(str(response).encode())
    # -- Close the data socket
    cs.close()

    if c_counter == 5:
        for address in range(0, len(client_address_list)):
            print("Client:" + str(address) + " Client IP, PORT" + str(client_address_list[address]))

# ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) esto hace que fuerze el puerto para que lo cierre y lo pueda usar
