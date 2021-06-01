from Client0 import Client
import Seq1

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 12100
c = Client(IP, PORT)
s = Seq1.Seq()
s.read_fasta('U5')

print("Sending  the U5 Gene to the server...")
print(s.strbases)
print(c.talk(s))
