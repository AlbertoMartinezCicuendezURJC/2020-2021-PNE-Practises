from Seq1 import Seq, test_sequences

def print_result(i, sequence):
    print("Sequence " + str(i) + " (Length:" + str(sequence.len()) + ") " + str(sequence))
    print(sequence.count())

print("-----|Practice1 ,Exercise 6|-----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

list_seq = list(test_sequences())

for i in range(1, len(list_seq) + 1):
    print_result(i, list_seq[i - 1])