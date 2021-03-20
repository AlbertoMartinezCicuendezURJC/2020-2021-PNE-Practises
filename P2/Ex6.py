from Client0 import Client
from pathlib import Path
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 12100


c = Client(IP, PORT)
s = Seq()
s.read_fasta("FRAT1")
count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i: i + 10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    print(c.talk(fragment))
