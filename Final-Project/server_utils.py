from Seq1 import Seq
from pathlib import Path
import colorama
import termcolor
import jinja2
import http.client
import json

list_sequences = ["TGACGATCGATCGACTG",
                  "CGATCGATCGATCGATCGATCAGTC",
                  "GACTCGATCGATCGATCGATCGATCG",
                  "TATTAGCGGCTAGCTAGCTGATCCACAGTGCATG",
                  "GCAGTCTGCTGCATGACTGACGTACTGCACAGTCAGTCAGT"]

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/assembly/'
ENDPOINT2 = '/info/species/'
PARAMS = '?content-type=application/json'
NOT_FOUND_ERROR = 'Specie not found!'
FAIL_CONNECTION_ERROR = 'Check if the ENDPOINT was correctly written!'

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

def esembl(ID, chr):
    connection = http.client.HTTPConnection(SERVER)
    connection.request('GET', ENDPOINT + ID + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        if chr == '':
            response = json.loads(response.read().decode())
            return response['karyotype']

        else:
            response = json.loads(response.read().decode())
            for dict in response['top_level_region']:
                if dict['name'] == chr:
                    return dict['length']

    elif response.status == 404:
        return FAIL_CONNECTION_ERROR
    else:
        return NOT_FOUND_ERROR

def print_karyotype(specie):
    context = {}
    information = esembl(specie, "")
    if information != NOT_FOUND_ERROR and information != FAIL_CONNECTION_ERROR:
        context['karyotype'] = information
        contents = read_template_htm_file('./html/info/karyotype.html').render(context=context)
        return contents
    else:
        context['error_msg'] = information
        context['specie'] = specie
        contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
        return contents

def print_chr_length(specie, chr):
    context = {}
    information = esembl(specie, chr)
    if information != NOT_FOUND_ERROR and information != FAIL_CONNECTION_ERROR:
        context['specie'] = specie
        context['chr'] = chr
        context['len'] = information
        contents = read_template_htm_file('./html/info/chrlength.html').render(context=context)
        return contents
    else:
        context['error_msg'] = information
        context['specie'] = specie
        contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
        return contents

def print_limit_species(limit):
    pass

