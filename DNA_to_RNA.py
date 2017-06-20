"""" convert DNA sequences to RNA """
def rna(seq):
    """convert a DNA sequence to RNA."""

    seq = seq.replace('t', 'u')

    # determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    #convert to lowercase
    seq = seq.lower()

    # swap out 't' for 'u'
    seq = seq.replace('t', 'u')

    # return upper or lower, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq



def reverse_rna_complement(seq):
    """"convert a DNA seq into itr reverse compl as RNA """

    #determine if the original se was uppercase
    seq_upper = seq.isupper()

    #reverse sequence
    rev_seq = seq[::-1]

    #convert to uppercase
    seq = seq.upper()

    # compute compelment
    rev_seq = rev_seq.replace('A', 't')
    rev_seq = rev_seq.replace('T', 'a')
    rev_seq = rev_seq.replace('G', 'c')
    rev_seq = rev_seq.replace('C', 'g')

    #return in appropriate case:
    if seq_upper:
        return seq.upper()
    else:
        return seq
