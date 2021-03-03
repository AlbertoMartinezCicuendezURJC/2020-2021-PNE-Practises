class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("This are the bases: ", self.strbases)

    def __str__(self): #print the object
        return self.strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq): #seq es el parent y Gene es el child. Gene hereda todos los methods del parent
    pass


s1 = Seq("AGTCGATCGATCG")
s2 = Seq("CAGT")
g = Gene("CGATCGACTAGCTGACTAGCTCAG")

print(f"Sequence 1: {s1}")  #esta y la de abajo es lo mismo
print("Sequence 1: {}".format(s1))
print(f"  Lenght 1: {s1.len()}")
print(f"Sequence 1: {s2}")
print(f"  Lenght 2: {s2.len()}")
print(f"Gene : {g}")