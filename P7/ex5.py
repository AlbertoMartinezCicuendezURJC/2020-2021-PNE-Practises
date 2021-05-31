import http.client
import json
import Seq1
import termcolor

GENES_DICT = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060'
              ,'RNU6_269P': 'ENSG00000212379', 'MIR633': 'ENSG00000207552', 'TTTY4C':'ENSG00000228296','RBMY2YP': 'ENSG00000227633'
              ,'FGFR3': 'ENSG00000068078', 'KDR': 'ENSMUSG00000062960', 'ANK2':'ENSG00000145362'}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
ID = GENES_DICT['MIR633']
PARAMS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
try:
    for id in GENES_DICT.values():
        connection.request('GET', ENDPOINT + id + PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            #print(json.dumps(response_dict, indent=4, sort_keys=True))
            sequence = Seq1.Seq(response_dict['seq'])
            s_lenght = sequence.len()
            a, c, g, t = sequence.percentages()
            s_most_repeated_base = sequence.most_repeated_base()
            print('Sequence:', sequence)
            print('Lenght:', s_lenght)
            print('Percentages of A, C, G, T respectively are:', a, c, g, t)  #mejorar este codigo para que imprima mejor
            print('Most repeated base is:', s_most_repeated_base)
except KeyError:
    print('Error')

