import Seq0

FOLDER = "./sequences/"
ID = "ADA"

filename = "sequences/U5"
U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
print("The first 20 bases are:", U5_seq[:20])






#dots represents folders (one dot= you go to the parent folder, in this case PO)
#2 dots, the parent of P0, 2020-2021