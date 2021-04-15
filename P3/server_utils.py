from Seq1 import Seq
from pathlib import Path
import colorama
import termcolor


GENE_FOLDER = "./sequences3/"


def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def coloured_text(message):
    if message == "GET":
        print_colored("GET", "green")
    elif message == "PING":
        print_colored("PING command!", "green")
    elif message == "INFO":
        print_colored("INFO", "green")
    elif message == "COMP":
        print_colored("COMP", "green")
    elif message == "REV":
        print_colored("REV", "green")
    else:
        print_colored("GENE", "green")

def format_command(command): # esto es porque al final, si pones por ejemplo PING, siempre habra un \r\n al final
    return command.replace("\n", "").replace("\r", "")

def lenght_and_percentages(sequence):
    s = Seq(sequence)
    lenght_sequence = s.len()
    a, c, g, t = s.count_bases()
    a_percentage = (a / s.len()) * 100
    c_percentage = (c / s.len()) * 100
    g_percentage = (g / s.len()) * 100
    t_percentage = (t / s.len()) * 100
    return lenght_sequence, a, c, g, t, a_percentage, c_percentage, g_percentage, t_percentage


def print_info(sequence):
    lenght_sequence, a, c, g, t, a_percentage, c_percentage, g_percentage, t_percentage = lenght_and_percentages(sequence)
    return "Sequence: " + str(sequence) + "\n" + "Lenght: " + str(lenght_sequence) + "\n" + "A: " + str(a) + " (" + str(a_percentage) + ") " + "\n" + "C: " + str(c) + " (" + str(c_percentage) + ") " + "\n" + "G: " + str(g) + " (" + str(g_percentage) + ") " + "\n" + "T: " + str(t) + " (" + str(t_percentage) + ") " + "\n"

def complement_seq(sequence):
    s = Seq(sequence)
    return s.complement()

def reversed_seq(sequence):
    s = Seq(sequence)
    return s.reverse()

def read_sequence(gene):
    loaded_gene = Seq.take_out_first_line(Path(GENE_FOLDER + gene).read_text())
    return loaded_gene