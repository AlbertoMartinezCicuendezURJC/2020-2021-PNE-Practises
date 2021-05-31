import json
import http.client

class Ensembl:

    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/info/assembly/'
    ENDPOINT2 = '/info/species/'
    ENDPOINT3 = '/sequence/id/'
    PARAMS = '?content-type=application/json'
    NOT_FOUND_ERROR = 'Specie not found!'
    FAIL_CONNECTION_ERROR = 'Check if the ENDPOINT was correctly written!'

    def __init__(self, specie, chr, limit, gene):
        self.specie = specie
        self.chr = chr
        self.limit = limit
        self.gene = gene

    def ensembl3(self):
        connection = http.client.HTTPConnection(Ensembl.SERVER)
        connection.request('GET', Ensembl.ENDPOINT3 + self.gene + Ensembl.PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            response = json.loads(response.read().decode())
            return response

        elif response.status == 404:
            return Ensembl.FAIL_CONNECTION_ERROR
        else:
            return Ensembl.NOT_FOUND_ERROR



e = Ensembl('', '', '', 'ENSG00000157764')

print(e.ensembl3())