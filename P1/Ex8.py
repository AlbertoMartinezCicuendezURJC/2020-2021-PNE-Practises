from Seq1 import Seq, test_sequences

def print_result(sequence):
    print("Sequence: (Length:" + str(sequence.len()) + ") " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Comp:", sequence.complement())

print("-----|Practice1 ,Exercise 5|-----")
FOLDER_NAME = "./sequences2/"
s = Seq()
s.read_fasta(FOLDER_NAME + "U5")
print_result(s)

