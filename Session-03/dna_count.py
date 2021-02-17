def correct_dna(seq):
    for c in seq:
        if c != "A" or c != "C" or c != "G" or c != "T":
            return False
    return True


def info_seq(seq):
    a_counter = 0
    g_counter = 0
    c_counter = 0
    t_counter = 0
    for element in range(0 ,len(seq)):
        if seq[element] == "A":
            a_counter += 1
        elif seq[element] == "G":
            g_counter += 1
        elif seq[element] == "C":
            c_counter += 1
        else:
            t_counter += 1
    return a_counter, c_counter, g_counter, t_counter

def print_info():
    a_counter, c_counter, g_counter, t_counter = info_seq(seq)
    return "A: " + str(a_counter) + "\n" + "C: " + str(c_counter) + "\n" + "G: " + str(g_counter) + "\n" + "T: " + str(t_counter)

seq = input("Write a sequence: ")
if correct_dna(seq):
    print(print_info())
    print("The lenght is:", len(seq))
else:
    print("The sequence is not valid")


#Una forma mejor en vez de poner a_count... -----> a, c, g, t = 0, 0, 0, 0