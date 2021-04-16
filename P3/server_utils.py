from Seq1 import Seq
from pathlib import Path
import colorama
import termcolor

list_sequences = ["TGACGATCGATCGACTG", "CGATCGATCGATCGATCGATCAGTC", "GACTCGATCGATCGATCGATCGATCG", "TATTAGCGGCTAGCTAGCTGATCCACAGTGCATG", "GCAGTCTGCTGCATGACTGACGTACTGCACAGTCAGTCAGT"]
GENE_FOLDER = "./sequences3/"


def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def coloured_text(message):
    if message == "GET":
        print_colored(message, "green")
    elif message == "PING":
        print_colored("PING command!", "green")
    elif message == "INFO":
        print_colored(message, "green")
    elif message == "COMP":
        print_colored(message, "green")
    elif message == "REV":
        print_colored(message, "green")
    else:
        print_colored("GENE", "green")

def format_command(command): # esto es porque al final, si pones por ejemplo PING, siempre habra un \r\n al final
    return command.replace("\n", "").replace("\r", "")

def get_seq(number):
    if 0 <= int(number) <= 4:
        return list_sequences[int(number)]
    else:
        return "Given number is out of range. Please, select a number between 0 and 4."


def complement_seq(sequence):
    s = Seq(sequence)
    return s.complement()

def info_seq(sequence):
    s = Seq(sequence)
    seq_information = s.print_info(sequence)
    return seq_information

def reversed_seq(sequence):
    s = Seq(sequence)
    return s.reverse()

def read_sequence(gene):
    loaded_gene = Seq.take_out_first_line(Path(GENE_FOLDER + gene).read_text())
    return loaded_gene
