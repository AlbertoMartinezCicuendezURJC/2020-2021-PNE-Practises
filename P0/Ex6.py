import Seq0

GENE_FOLDER = "./sequences/"

print("-----| Exercise 6 |------")
sequence = Seq0.seq_read_fasta(GENE_FOLDER + "U5")
print("Frag:", sequence[:20])
print("Rev:", Seq0.seq_reverse(sequence[:20]))