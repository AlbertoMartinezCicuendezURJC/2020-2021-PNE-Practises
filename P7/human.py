import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/assembly/'
#ID = 'homo_sapiens'
PARAMS = '?content-type=application/json'

def http_server(ID):
    connection = http.client.HTTPConnection(SERVER)
    connection.request('GET', ENDPOINT + ID + PARAMS)
    response = connection.getresponse()
    print('Response received!', response.status, response.reason)
    if response.status == 200:
        response = json.loads(response.read().decode())
        return response

    elif response.status == 404:
        return 'Check if the ENDPOINT was correctly written!'
    else:
        return 'Specie not found'

print(http_server('homo_sapiens'))


    # diria que es hacer una funcion con un http.client