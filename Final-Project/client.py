import http.client
import json
import termcolor
from ensembl_class import Ensembl
from Seq1 import Seq

PORT = 8080
SERVER = 'localhost'
PARAM = '&json=1'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

endpoint1 = "/listSpecies?limit=6"

try:
    conn.request("GET", endpoint1 + PARAM) # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

limit_response = conn.getresponse()
print(f"Response received!: {limit_response.status} {limit_response.reason}\n")

limit_dict = json.loads(limit_response.read().decode())


limit = endpoint1.split('?')[1].split('=')[1].split('&')[0]
termcolor.cprint('The first ' + limit + ' species are:', 'magenta')
if limit == '':
    limit = Ensembl.counter_species()
for n in range(0, int(limit)):
    termcolor.cprint(limit_dict['species'][n]['display_name'], 'blue')
termcolor.cprint('=============================================================================', 'green')



endpoint2 = "/karyotype?specie=mouse"
try:
    conn.request("GET", endpoint2 + PARAM) # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

karyotype_response = conn.getresponse()
print(f"Response received!: {karyotype_response.status} {karyotype_response.reason}\n")
dict_karyotype = json.loads(karyotype_response.read().decode())

specie = endpoint2.split('?')[1].split('=')[1].split('&')[0]
termcolor.cprint('The karyotype of ' + specie + ' is:', 'magenta')
for chromosome in dict_karyotype['karyotype']:
    termcolor.cprint(chromosome, 'blue')
termcolor.cprint('=============================================================================', 'green')



endpoint3 = "/chromosomeLength?specie=mouse&chromo=X"
try:
    conn.request("GET", endpoint3 + PARAM) # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

chr_length_response = conn.getresponse()
print(f"Response received!: {chr_length_response.status} {chr_length_response.reason}\n")

chr_length_dict = json.loads(chr_length_response.read().decode())
specie2 = endpoint3.split('?')[1].split('=')[1].split('&')[0]
chr = endpoint3.split('?')[1].split('=')[2].split(' ')[0].split('&')[0]

for dict in chr_length_dict['top_level_region']:
    if dict['name'] == chr:
        lenght = dict['length']

termcolor.cprint('The specie selected was: ', 'magenta', end='')
termcolor.cprint(specie2, 'blue')
termcolor.cprint('The chromosome selected was: ', 'magenta', end='')
termcolor.cprint(chr, 'blue')
termcolor.cprint('The chromosome lenght is: ', 'magenta', end='')
termcolor.cprint(str(lenght), 'blue')
termcolor.cprint('=============================================================================', 'green')



endpoint4 = "/geneSeq?gene=FRAT1"
try:
    conn.request("GET", endpoint4 + PARAM)  # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

seq_response = conn.getresponse()
print(f"Response received!: {seq_response.status} {seq_response.reason}\n")

seq_dict = json.loads(seq_response.read().decode())
gene = endpoint4.split('?')[1].split('=')[1].split('&')[0]

termcolor.cprint('GENE ', 'magenta', end='')
termcolor.cprint(gene, 'blue')
termcolor.cprint('Its sequence is ', 'magenta', end='')
termcolor.cprint(seq_dict['seq'], 'blue')
termcolor.cprint('=============================================================================', 'green')



endpoint5 = "/geneInfo?gene=ADA"
try:
    conn.request("GET", endpoint5 + PARAM)  # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

info_response = conn.getresponse()
print(f"Response received!: {info_response.status} {info_response.reason}\n")

info_dict = json.loads(info_response.read().decode())
gene2 = endpoint5.split('?')[1].split('=')[1].split('&')[0]
gene2_object = Seq(info_dict['seq'])

termcolor.cprint('GENE ', 'magenta', end='')
termcolor.cprint(gene2, 'blue')

termcolor.cprint('The beginning of the gene is: ', 'magenta', end='')
termcolor.cprint(info_dict['desc'].split(':')[3], 'blue')

termcolor.cprint('The end of the gene is:  ', 'magenta', end='')
termcolor.cprint(info_dict['desc'].split(':')[4], 'blue')

termcolor.cprint('The chromosome name is: ', 'magenta', end='')
termcolor.cprint(info_dict['desc'].split(':')[1], 'blue')

termcolor.cprint('The ID is: ', 'magenta', end='')
termcolor.cprint(info_dict['id'], 'blue')

termcolor.cprint('The length is: ', 'magenta', end='')
termcolor.cprint(gene2_object.len(), 'blue')
termcolor.cprint('=============================================================================', 'green')



endpoint6 = "/geneCalc?gene=FXN"
try:
    conn.request("GET", endpoint6 + PARAM)  # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

calc_response = conn.getresponse()
print(f"Response received!: {calc_response.status} {calc_response.reason}\n")

calc_dict = json.loads(calc_response.read().decode())
gene3 = endpoint6.split('?')[1].split('=')[1].split('&')[0]
gene3_object = Seq(calc_dict['seq'])
a_perc, c_perc, g_perc, t_perc = gene3_object.percentages()

termcolor.cprint('GENE ', 'magenta', end='')
termcolor.cprint(gene3, 'blue')

termcolor.cprint('The total length of the gene is: ', 'magenta', end='')
termcolor.cprint(gene3_object.len(), 'blue')

termcolor.cprint('The percentage of the base "A": ', 'magenta', end='')
termcolor.cprint(str(a_perc) + '%', 'blue')

termcolor.cprint('The percentage of the base "C": ', 'magenta', end='')
termcolor.cprint(str(c_perc) + '%', 'blue')

termcolor.cprint('The percentage of the base "G": ', 'magenta', end='')
termcolor.cprint(str(g_perc) + '%', 'blue')

termcolor.cprint('The percentage of the base "T": ', 'magenta', end='')
termcolor.cprint(str(t_perc) + '%', 'blue')
termcolor.cprint('=============================================================================', 'green')



