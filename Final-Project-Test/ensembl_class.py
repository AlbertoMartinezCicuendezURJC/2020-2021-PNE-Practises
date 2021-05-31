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
    GENES_DICT = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060',
                  'RNU6_269P': 'ENSG00000212379', 'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296',
                  'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078', 'KDR': 'ENSMUSG00000062960', 'ANK2': 'ENSG00000145362'}

    def __init__(self, specie, chr, limit, gene):
        self.specie = specie
        self.chr = chr
        self.limit = limit
        self.gene = gene

    def ensembl(self):
        connection = http.client.HTTPConnection(Ensembl.SERVER)
        connection.request('GET', Ensembl.ENDPOINT + self.specie + Ensembl.PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            if self.chr == '':
                response = json.loads(response.read().decode())
                return response['karyotype']

            else:
                response = json.loads(response.read().decode())
                for dict in response['top_level_region']:
                    if dict['name'] == self.chr:
                        return dict['length']

        elif response.status == 404:
            return Ensembl.FAIL_CONNECTION_ERROR
        else:
            return Ensembl.NOT_FOUND_ERROR

    @staticmethod
    def counter_species():
        connection = http.client.HTTPConnection(Ensembl.SERVER)
        connection.request('GET', Ensembl.ENDPOINT2 + Ensembl.PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            response = json.loads(response.read().decode())
            counter = 0
            for n in response['species']:
                counter += 1
            return counter

    def ensembl2(self):
        connection = http.client.HTTPConnection(Ensembl.SERVER)
        connection.request('GET', Ensembl.ENDPOINT2 + Ensembl.PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            response = json.loads(response.read().decode())
            specie_name_list = []

            for n in range(0, self.limit):
                specie_name_list.append(response['species'][n]['display_name'])
            return specie_name_list, Ensembl.counter_species()

        elif response.status == 404:
            return Ensembl.FAIL_CONNECTION_ERROR

        else:
            return Ensembl.NOT_FOUND_ERROR

    def ensembl3(self):
        connection = http.client.HTTPConnection(Ensembl.SERVER)
        connection.request('GET', Ensembl.ENDPOINT3 + Ensembl.GENES_DICT[self.gene] + Ensembl.PARAMS)
        response = connection.getresponse()
        if response.status == 200:
            response = json.loads(response.read().decode())
            return response

        elif response.status == 404:
            return Ensembl.FAIL_CONNECTION_ERROR
        else:
            return Ensembl.NOT_FOUND_ERROR



