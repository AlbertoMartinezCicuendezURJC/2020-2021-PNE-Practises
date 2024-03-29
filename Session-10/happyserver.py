import socket

PORT = 8080
IP = "localhost"
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
    print("CONNECTION: "+ str(c_counter) + " CLient IP, PORT: " + str(client_ip_port))
    print("A client has connected to the server!")

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    # -- Print the received message
    print(f"Message received: {msg}")

    # -- Send a response message to the client
    try:
        response = int(msg) ** int(msg)

        # -- The message has to be encoded into bytes
        cs.send(str(response).encode())
    except ValueError:
        response = "We need a number"
        cs.send(response.encode())
    # -- Close the data socket
    cs.close()

    if c_counter == 5:
        for address in range(0, len(client_address_list)):
            print("Client:" + str(address) + " Client IP, PORT" + str(client_address_list[address]))
        exit(0)

# ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) esto hace que fuerze el puerto para que lo cierre y lo pueda usar