class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("This are the bases: ", self.strbases)

    def __str__(self): #print the object
        return self.strbases

s1 = Seq("AGTCGATCGATCG")
s2 = Seq("CAGT")

print(f"Sequence 1: {s1}")
print(f"Sequence 1: {s2}")