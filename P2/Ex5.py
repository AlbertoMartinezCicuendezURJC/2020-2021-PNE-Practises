from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 12100


c = Client(IP, PORT)
print(c.talk("Sending  the U5 Gene to the server..."))
print(c.talk(Path("U5").read_text()))
