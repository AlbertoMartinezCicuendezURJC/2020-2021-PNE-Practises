from Client_class import Client
from server_utils import list_sequences



gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("-----| Practice 3, Exercise 7 |------")

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)

correct = False
while not correct:
    msg = input("What do you want to know: ")

    if msg == "PING":
        print(c.talk(msg))

    elif msg == "GET":
        print("Testing GET...")
        for i in range(0, 5):
            print(msg, i)
            print(c.talk(msg + " " + str(i)))

    elif msg == "INFO" or msg == "COMP" or msg == "REV":
        print("Testing " + msg + "...")
        print(c.talk(msg + " " + list_sequences[0]))

    elif msg == "GENE":
        print("Testing GENES...")
        for list in gene_list:
            print("GENE " + list)
            print(c.talk("GENE " + list) + "\n")

    elif msg.lower() == "exit":
        correct = True
        print("Hope this information helps you!")
    else:
        print("This command is not available. Please, choose a correct one.")