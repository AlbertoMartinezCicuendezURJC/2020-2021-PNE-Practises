from Client0 import Client


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 12100

c = Client(IP, PORT)
print(c.debug_talk("Funciona porfi"))
