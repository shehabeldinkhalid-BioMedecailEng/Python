def DNA_COMP(stander):
    stander = str(stander).upper()
    for Nuc in stander:
        if ( Nuc == "A" ):
            Nuc = "T"
            print(Nuc)
        elif ( Nuc == "T" ):
            Nuc = "A"
            print(Nuc)
        elif ( Nuc == "C" ):
            Nuc = "G"
            print(Nuc)
        elif ( Nuc == "G" ):
            Nuc = "C"
            print(Nuc)
        else:
            Nuc = Nuc
            print(Nuc)
# ----------------------------------------------------------------------------------------------
import random
def generate_dna_sequence(n):
    # نختار بشكل عشوائي من A,T,G,C
    print(''.join(random.choice(["A","T","G","C"]) for _ in range(n)))

#---------------------------------------------------------------------------------------------

def valid_DNA(stander):
    stander = str(stander).upper()
    check = True
    for Nuc in stander:    
        if ( Nuc!="A" or Nuc!="T" or Nuc!="G" or Nuc!="C"):
            check=False
            break
    if ( check == True ):
            print("Valid")
    else:
            print("Not valid")
# ---------------------------------------------------------------------------------------------
def generate_random_dna(size:int)->str:
    sequence_list = []
    nucleotides = ['A', 'G', 'C', 'T']
    # 
    for i in range(size):
        random_choice = random.choice(nucleotides) 
        # then add new nucleotides to the list 
        sequence_list.append(random_choice) 
    sequence_str = "".join(sequence_list)
    return sequence_str
# -----------------------------------------------------------------------------------------------------------
def generate_random_rna(size:int)->str:
    sequence_list = []
    nucleotides = ['A', 'G', 'C', 'U']
    for i in range(size):
        random_choice = random.choice(nucleotides)
        sequence_list.append(random_choice)
    sequence_str = "".join(sequence_list)
    return sequence_str
# -----------------------------------------------------------------------------------------------------------
def count_nucleotides(s):
    counter = 0
    for Nuc in s:
        if (Nuc == "A" or Nuc == "T" or Nuc == "G" or Nuc == "C" ):
            counter += 1
    return counter
# -----------------------------------------------------------------------------------------------------------
def split_seq1(seq, n):
    for i in range(0, len(seq), n):
        print(seq[i:i+n])
        sequ = [].append(seq[i:i+n])
    return sequ
# -----------------------------------------------------------------------------------------------------------
def transcribe_dna(s, status):
    if status == "coding":
        return s.replace('T', 'U')
    return DNA_COMP(s).replace('T', 'U')

# -----------------------------------------------------------------------------------------------------------
def translate_dna(rna):
    aa = []
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if codon in ('UAA', 'UAG', 'UGA'):
            break
        if codon == 'AUG':
            aa.append('M')
        elif codon in ('UUU', 'UUC'):
            aa.append('F')
        else:
            aa.append('?')
    return ''.join(aa)



DNA_COMP
translate_dna
split_seq1
generate_random_rna
valid_DNA
count_nucleotides
generate_random_dna
transcribe_dna