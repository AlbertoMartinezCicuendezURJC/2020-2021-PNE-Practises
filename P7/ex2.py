import http.client
import json

GENES_DICT = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060'
              ,'RNU6_269P': 'ENSG00000212379', 'MIR633': 'ENSG00000207552', 'TTTY4C':'ENSG00000228296','RBMY2YP': 'ENSG00000227633'
              ,'FGFR3': 'ENSG00000068078', 'KDR': 'ENSMUSG00000062960', 'ANK2':'ENSG00000145362'}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
ID = GENES_DICT['FRAT1']
PARAMS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
connection.request('GET', ENDPOINT + ID + PARAMS)
response = connection.getresponse()
print('Response received!', response.status, response.reason)
if response.status == 200:
    response = json.loads(response.read().decode())
    #print(json.dumps(response, indent=4, sort_keys=True)) para que se printee + ordenado
    print('Gene:', ID)
    print('Description:', response['desc'].split(':'))
    print('Bases:', response['seq'])
elif response.status == 404:
    print('Check if the ENDPOINT was correctly written!')