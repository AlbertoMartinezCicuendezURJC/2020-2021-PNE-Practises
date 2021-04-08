import Client0

c = Client0.Client("localhost", 8080)
for i in range(0, 5):
    c.talk("Message " + str(i))