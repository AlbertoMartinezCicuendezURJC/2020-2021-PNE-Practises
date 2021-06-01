import socket
import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self): #test if the IP works, that the server is running
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up!")
        except ConnectionRefusedError:
            print("You could not connect to the server")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.

        s.send(str(msg).encode())

        # Receive data
        response = s.recv(2048).decode("utf-8") #esto es como un block, hasta que no haya mensajes aqui te quedas

        # Close the socket
        s.close()

        # Return the response
        return response

    def debug_talk(self, msg):
        response = self.talk(msg)
        print("To server:", end=" ")
        termcolor.cprint(msg, "yellow")
        print("From server:", end=" ")
        termcolor.cprint(response, "blue")
        return ""








