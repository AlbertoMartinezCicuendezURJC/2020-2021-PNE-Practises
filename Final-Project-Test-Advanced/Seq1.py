from pathlib import Path
import termcolor

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


def is_valid_sequence(strbases):
    for c in strbases:
        if c != "A" and c != "G" and c != "T" and c != "C":
            return False
        else:
            return True



class Seq:

    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"
    ERROR_MSG = "Invalid sequence. Please, choose a correct one."

    def __init__(self, strbases=NULL_SEQUENCE):

        if strbases == "NULL":
            self.strbases = strbases
            print("NULL Seq created!")

        else:
            if Seq.is_valid_sequence_2(strbases):
                self.strbases = strbases
                print("New sequence created!")

            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")


    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "G" and c != "T" and c != "C":
                return False
            else:
                return True

    @staticmethod
    def is_valid_sequence_2(bases):
        count_errors = 0
        for c in bases:
            if c != "A" and c != "G" and c != "T" and c != "C":
                count_errors += 1
        if count_errors != 0:
            return False
        else:
            return True

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == Seq.INVALID_SEQUENCE or self.strbases == Seq.NULL_SEQUENCE:
            return 0
        else:
            return len(self.strbases)


    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)):
            text = "Sequence" + str(i) + ":(Lenght:" + str(seq_list[i].len()) + ")" + str(seq_list[i])
            termcolor.cprint(text, "yellow")

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t

        else:
            for base in self.strbases:
                if base == "A":
                    a += 1
                elif base == "C":
                    c += 1
                elif base == "G":
                    g += 1
                elif base == "T":
                    t += 1

            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "T": t, "G": g}

    def reverse(self):
        if self.strbases == Seq.INVALID_SEQUENCE or self.strbases == Seq.NULL_SEQUENCE:
            return Seq.ERROR_MSG
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.INVALID_SEQUENCE or self.strbases == Seq.NULL_SEQUENCE:
            return Seq.ERROR_MSG
        else:
            complement_seq = ""
            for base in self.strbases:
                if base == "A":
                    complement_seq += "T"
                elif base == "T":
                    complement_seq += "A"
                elif base == "C":
                    complement_seq += "G"
                else:
                    complement_seq += "C"
            return complement_seq

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    @staticmethod
    def take_out_first_line(sequence):
        return sequence[sequence.find("\n") + 1:].replace("\n", "")

    def most_repeated_base(self):
        a, c, g, t = self.count_bases()
        if max(a, c, g, t) == a:
            return "A"
        if max(a, c, g, t) == c:
            return "C"
        if max(a, c, g, t) == t:
            return "T"
        else:
            return "G"

    def percentages_and_length(self):
        a, c, g, t = self.count_bases()
        a_percentage = round((a / self.len()) * 100, 3)
        c_percentage = round((c / self.len()) * 100, 3)
        g_percentage = round((g / self.len()) * 100, 3)
        t_percentage = round((t / self.len()) * 100, 3)
        return a_percentage, c_percentage, g_percentage, t_percentage, self.len()

    def print_info(self, sequence):
        a, c, g, t = self.count_bases()
        a_percentage, c_percentage, g_percentage, t_percentage = self.percentages()
        return "Lenght: "+ str(self.len()) + "\n" + "A: " + str(a) + " (" + str(a_percentage) + ") " + "\n" + "C: " + str(c) + " (" + str(c_percentage) + ") " + "\n" + "G: " + str(g) + " (" + str(g_percentage) + ") " + "\n" + "T: " + str(t) + " (" + str(t_percentage) + ") " + "\n"


def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3


