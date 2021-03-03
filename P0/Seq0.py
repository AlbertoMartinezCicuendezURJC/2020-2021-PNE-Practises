from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    sequence = Path(filename).read_text()
    sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for d in seq:
        gene_dict[d] += 1
    return gene_dict

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    changed_seq = ""
    for base in seq:
        if base == "A":
            changed_seq += "T"
        elif base == "T":
            changed_seq += "A"
        elif base == "C":
            changed_seq += "G"
        else:
            changed_seq += "C"
    return changed_seq

def most_repeated_base(seq):
    a, c, g, t = 0, 0, 0, 0
    for base in seq:
        if base == "A":
            a += 1
        elif base == "T":
            t += 1
        elif base == "C":
            c += 1
        else:
            g += 1
    counter_list = [a, c, g, t]
    if max(counter_list) == a:
        return "A"
    elif max(counter_list) == c:
        return "C"
    elif max(counter_list) == g:
        return "G"
    else:
        return "T"
