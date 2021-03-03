import Seq0

GENE_FOLDER = "./sequences/"

print("-----| Exercise 7 |------")
sequence = Seq0.seq_read_fasta(GENE_FOLDER + "U5")
print("Frag:", sequence[:20])
print("Comp:", Seq0.seq_complement(sequence[:20]))