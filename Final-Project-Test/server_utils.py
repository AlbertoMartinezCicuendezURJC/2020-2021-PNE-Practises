from Seq1 import Seq
from pathlib import Path
import colorama
import termcolor
import jinja2
from ensembl_class import Ensembl
from Seq1 import Seq


def read_template_htm_file(filename):
    content = jinja2.Template(Path(filename).read_text())
    return content


def print_karyotype(specie):
    context = {}
    e = Ensembl(specie, '', '', '')
    information = e.ensembl()
    if information != Ensembl.NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
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
    e = Ensembl(specie, chr, '', '')
    information = e.ensembl()
    if information != Ensembl.NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
        context['specie'] = specie
        context['chr'] = chr
        context['len'] = information
        contents = read_template_htm_file('./html/info/chrlength.html').render(context=context)
        return contents
    else:
        context['type'] = 'specie'
        context['error_msg'] = information
        context['input'] = specie
        contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
        return contents


def print_limit(limit):
    try:
        context = {}
        e = Ensembl('', '', int(limit), '')
        information, counter = e.ensembl2()
        context['specie'] = information
        context['limit'] = limit
        context['counter'] = counter
        contents = read_template_htm_file('html/info/limitSpecies.html').render(context=context)
        return contents
    except ValueError:
        contents = read_template_htm_file('html/Error.html').render()
        return contents


def print_sequence(gene):
    context = {}
    e = Ensembl('', '', '', gene)
    try:
        information = e.ensembl3()
        if information != Ensembl.NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
            context['sequence'] = information['seq']
            context['gene'] = gene
            contents = read_template_htm_file('html/info/geneSeq.html').render(context=context)
            return contents
        else:
            context['type'] = 'gene'
            context['input'] = gene
            contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
            return contents
    except KeyError:
        contents = read_template_htm_file('html/Error.html').render()
        return contents


def print_info(gene):
    try:
        context = {}
        e = Ensembl('', '', '', gene)
        information = e.ensembl3()
        if information != Ensembl.NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
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
            context['type'] = 'gene'
            context['input'] = gene
            contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
            return contents
    except KeyError:
        contents = read_template_htm_file('html/Error.html').render()
        return contents


def print_length_percentages(gene):
    context = {}
    e = Ensembl('', '', '', gene)
    try:
        information = e.ensembl3()
        if information != Ensembl.NOT_FOUND_ERROR and information != Ensembl.FAIL_CONNECTION_ERROR:
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
            context['type'] = 'gene'
            context['input'] = gene
            contents = read_template_htm_file('html/dynamic_error.html').render(context=context)
            return contents
    except KeyError:
        contents = read_template_htm_file('html/Error.html').render()
        return contents





























