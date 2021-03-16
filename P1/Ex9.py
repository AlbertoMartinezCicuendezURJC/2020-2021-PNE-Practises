from Seq1 import Seq
from P0 import sequences

print("-----|Practice1 ,Exercise 5|-----")


s1 = Seq()
GENE_FOLDER = "./sequences2/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]


for gene in gene_list:
    s1.read_fasta(GENE_FOLDER + gene)
    print("Gene", gene, ":", "Most frequent Base:", s1.most_repeated_base())


