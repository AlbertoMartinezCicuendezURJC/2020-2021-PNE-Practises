from Seq1 import Seq
from P0 import sequences

print("-----|Practice1 ,Exercise 5|-----")

GENE_FOLDER = "./sequences2/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


for gene in gene_list:
    s = Seq()
    s.read_fasta(GENE_FOLDER + gene)
    print("Gene", gene, ":", "Most frequent Base:", s.most_repeated_base())


