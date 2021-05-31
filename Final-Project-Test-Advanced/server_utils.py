from pathlib import Path
import jinja2
from ensembl_class import Ensembl
from Seq1 import Seq


def read_template_htm_file(filename):
    content = jinja2.Template(Path(filename).read_text())
    return content


def print_karyotype(specie, param_json):
    context = {}
    e = Ensembl(specie, '', '', '')
    information = e.ensembl()

    if param_json:
        return information

    else:
        if information != Ensembl.SPECIE_NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
            information = information['karyotype']
            context['karyotype'] = information
            contents = read_template_htm_file('./html/info/karyotype.html').render(context=context)
            return contents
        else:
            context['error_msg'] = information
            context['type'] = 'specie'
            context['input'] = specie
            contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
            return contents


def print_chr_length(specie, chr, param_json):
    context = {}
    e = Ensembl(specie, chr, '', '')
    information = e.ensembl()
    if param_json:
        if information == Ensembl.SPECIE_NOT_FOUND_ERROR:
            return information
        else:
            if not chr.isdigit():
                return "The chromosome number '" + chr + "' is not a number. Please, choose an INTEGER number and try again."
            else:
                return information

    else:
        if information != Ensembl.SPECIE_NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
            for dict in information['top_level_region']:
                if dict['name'] == chr:
                    lenght = dict['length']
            try:
                context['specie'] = specie
                context['chr'] = int(chr)
                context['len'] = lenght
                contents = read_template_htm_file('./html/info/chrlength.html').render(context=context)
                return contents
            except ValueError:
                context['type'] = 'chromosome number'
                context['input'] = chr
                contents = read_template_htm_file('html/Numbers_error.html').render(context=context)
                return contents

        else:
            context['type'] = 'specie'
            context['error_msg'] = information
            context['input'] = specie
            contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
            return contents


def print_limit(limit):
    context = {}
    try:
        e = Ensembl('', '', int(limit), '')
        information, counter = e.ensembl2()
        context['specie'] = information
        context['limit'] = limit
        context['counter'] = counter
        contents = read_template_htm_file('html/info/limitSpecies.html').render(context=context)
        return contents
    except ValueError:
        context['type'] = 'limit'
        context['input'] = limit
        contents = read_template_htm_file('html/Numbers_error.html').render(context=context)
        return contents


def print_sequence(gene):
    context = {}
    e = Ensembl('', '', '', gene)
    information = e.ensembl3()
    if information != Ensembl.GENE_NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
        context['sequence'] = information['seq']
        context['gene'] = gene
        contents = read_template_htm_file('html/info/geneSeq.html').render(context=context)
        return contents

    else:
        context['error_msg'] = information
        context['type'] = 'gene'
        context['input'] = gene
        contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
        return contents


def print_info(gene):
    context = {}
    e = Ensembl('', '', '', gene)
    information = e.ensembl3()
    if information != Ensembl.GENE_NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
        s1 = Seq(information['seq'])
        context['gene'] = gene
        context['start'] = information['desc'].split(':')[3]
        context['end'] = information['desc'].split(':')[4]
        context['chromosome'] = information['desc'].split(':')[1]
        context['id'] = information['id']
        context['length'] = s1.len()
        contents = read_template_htm_file('html/info/geneInfo.html').render(context=context)
        return contents

    else:
        context['error_msg'] = information
        context['type'] = 'gene'
        context['input'] = gene
        contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
        return contents


def print_length_percentages(gene):
    context = {}
    e = Ensembl('', '', '', gene)
    information = e.ensembl3()
    if information != Ensembl.GENE_NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
        information = information['seq']
        s1 = Seq(information)
        a_percentage, c_percentage, g_percentage, t_percentage, length = s1.percentages_and_length()
        context['a_perc'] = a_percentage
        context['c_perc'] = c_percentage
        context['g_perc'] = g_percentage
        context['t_perc'] = t_percentage
        context['length'] = length
        contents = read_template_htm_file('html/info/geneCalc.html').render(context=context)
        return contents

    else:
        context['error_msg'] = information
        context['type'] = 'gene'
        context['input'] = gene
        contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
        return contents






























