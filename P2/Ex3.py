from Client0 import Client

from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 12100

c = Client(IP, PORT)
message = "Hello! How u doing?"
print("To server:", message)
print("Response:", c.talk(message))