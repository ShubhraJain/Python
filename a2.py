def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0
    for c in dna:
        if (c == nucleotide):
            count = count + 1
    return count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    for i in range(len(dna1) - 1):
        if (dna1[i:i+2] == dna2):
            return True
    return False

def is_valid_sequence(dna):
    """(str) -> bool

    Return true if the dna containes no characters other than A,T,C,and G

    >>> is_valid_sequence('ATCCA')
    True
    >>> is_valid_sequence('STAR')
    False
    
    """
    sequence = True
    for char in dna:
        if not (char == 'A' or char == 'T' or char == 'G' or char == 'C'):
            return False
    return sequence

def insert_sequence(dna, insert_sequence, index):
    """ (str, str, int) -> str

    Inserts the sequnce into dna at given index

    >>> insert_sequence('ATCC', 'GC', 1)
    AGCTCC
    
    """
    return (dna[:index] + insert_sequence + dna[index:])


    
def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of the nucleotide

    >>> get_complement('A')
    T
    >>> get_complement('G')
    C

    """
    if (nucleotide == 'A'):
        print ('T')
    elif (nucleotide == 'T'):
        print ('A')
    elif (nucleotide == 'G'):
        print ('C')
    else:
        print ('G')
    

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the compliment of the DNA sequence.

    >>> get_complementary_sequence('ATGC')
    TACG
    
    """
    l = []
    for char in dna:
        if (char == 'A'):
            l.append('T')
        elif (char == 'T'):
            l.append('A')
        elif (char == 'C'):
            l.append('G')
        else:
            l.append('C')
    return "".join(l)

    
