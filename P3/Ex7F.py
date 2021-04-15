from Client_class import Client

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6-269P"]
print("-----| Practice 3, Exercise 7 |------")

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)

msg = input("What do you want to know: ")

if msg == "PING":
    print(c.talk(msg))

elif msg == "GET":
    print("Testing GET...")
    for i in range(0, 5):
        print(msg, i, end=" ")
        print(c.talk("GET " + str(i)))

elif msg == "INFO" or msg == "COMP" or msg == "REV":
    print("Testing " + msg + "...")
    print(c.talk(msg + " TGACGATCGATCGACTG"))

elif msg == "GENE":
    print("Testing GENES...")
    for list in gene_list:
        print("GENE " + list)
        print(c.talk("GENE " + list))
else:
    print("This command is not available. Please, choose a correct one.")