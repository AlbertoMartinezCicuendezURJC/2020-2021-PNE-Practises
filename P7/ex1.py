import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'

connection = http.client.HTTPConnection(SERVER)
connection.request('GET', ENDPOINT + PARAMS)
response = connection.getresponse()
#print(response.read()) # esto te da una b de bytes, so:
#print(response.read().decode()) #pero esto da una string porque es lo que hace el decode
answer_decoded = response.read().decode()
dict_response = json.loads(answer_decoded)
print(dict_response)
if dict_response['ping'] == 1:
    print('PING OK!')
else:
    print('ERROR')
