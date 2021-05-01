from Seq1 import Seq
from pathlib import Path
import colorama
import termcolor
import jinja2
list_sequences = ["TGACGATCGATCGACTG",
                  "CGATCGATCGATCGATCGATCAGTC",
                  "GACTCGATCGATCGATCGATCGATCG",
                  "TATTAGCGGCTAGCTAGCTGATCCACAGTGCATG",
                  "GCAGTCTGCTGCATGACTGACGTACTGCACAGTCAGTCAGT"]

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

def get_seq(list_sequences, number):
    context = {'number': number, 'sequence': list_sequences[int(number)]}
    contents = read_template_htm_file('./html/get.html').render(context=context)
    return contents

def gene(seq_name):
    PATH = "./sequences/" + seq_name
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {"gene_name": seq_name, "gene_contents":s1.strbases}
    contents = read_template_htm_file("./html/gene.html").render(context=context)
    return contents

def complement_seq(sequence):
    s = Seq(sequence)

    if s.complement() != Seq.ERROR_MSG:
        context = {'sequence': sequence, 'result': s.complement(), 'operation': 'Complement'}
        contents = read_template_htm_file('./html/complement.html').render(context=context)
    else:
        context = {'sequence':sequence, 'message_error':Seq.ERROR_MSG}
        contents = read_template_htm_file('./html/invalid_seqs.html').render(context=context)
    return contents

def info_seq(sequence):
    s = Seq(sequence)
    if s.complement() != Seq.ERROR_MSG:
        context = {'sequence': sequence, 'result': s.print_info(sequence), 'operation': 'Information'}
        contents = read_template_htm_file('./html/info.html').render(context=context)
    else:
        context = {'sequence': sequence, 'message_error': Seq.ERROR_MSG}
        contents = read_template_htm_file('./html/invalid_seqs.html').render(context=context)
    return contents

def reversed_seq(sequence):
    s = Seq(sequence)

    if s.complement() != Seq.ERROR_MSG:
        context = {'sequence': sequence, 'result': s.reverse(), 'operation': 'Reverse'}
        contents = read_template_htm_file('./html/reversed.html').render(context=context)
    else:
        context = {'sequence': sequence, 'message_error': Seq.ERROR_MSG}
        contents = read_template_htm_file('./html/invalid_seqs.html').render(context=context)
    return contents

def read_template_htm_file(filename):
    content = jinja2.Template(Path(filename).read_text())
    return content