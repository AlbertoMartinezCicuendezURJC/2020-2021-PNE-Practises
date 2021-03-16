class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid_sequence():
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "Error"
            print("INCORRECT sequence detected")

    @staticmethod  # --- We are creating a function inside a class, not a method
    def print_seqs(list_seq, color):
        for i in range(0, len(list_seq)):
            text = "sequence " + str(i) + ":" + " Length:" + str(list_seq[i].len()) + " " + str(list_seq[i])
            termcolor.cprint(text, color)

    # -- Because the next function has no @staticmethod we are creating methods
    def is_valid_sequence(self):
        for c in self.strbases:
            if c != "A" and c != "C" and c != "G" and c != "T":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)