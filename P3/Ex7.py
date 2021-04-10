from Client_class import Client

print("-----| Practice 3, Exercise 7 |------")

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)


print("Testing INFO...")
print(c.talk("INFO GGGGATTATATTCTCTCTTGAGAGAG"))
print("\n")

print("Testing COMP...")
print(c.talk("COMP TTGGCATTCAGCATCAT"))
print("\n")

print("Testing REV...")
print(c.talk("REV ATCAGTCATCGATCGAT"))
print("\n")

print("Testing GENES...")
print("U5:", c.talk("GENE U5"))
print("\n")
print("FRAT1:", c.talk("GENE FRAT1"))