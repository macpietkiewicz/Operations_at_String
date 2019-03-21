import random
out = open("2_wyniki.txt", 'w')
lenght = 100
"""--------------------FUNKCJE--------------------------------------------------"""
def Sequence():     #generowanie losowej sekwencji nukleotydowej o długoci lenght
    dna = []
    for i in range(lenght):
        dna += random.choice(['A','T','C','G'])
    print("Sekwencja DNA wygenerowana  losowo  \n", ''.join(dna), file = out)
    return(''.join(dna))
    
def ComplementarSequence(dna):  #generowanie sekwencji komplementarnej do początkowej sekwencji DNA
    complementar=[]
    for nucleotide in dna:   
        if nucleotide == 'A':
            complementar.append('T')
        elif nucleotide == 'T':
            complementar.append('A')
        elif nucleotide == 'C':
            complementar.append('G')
        elif nucleotide == 'G':
            complementar.append('C')
        else:
            pass
    print("Nić komplementarna:\n\n3'-",''.join(complementar),"-5'", "\n", file = out)
    return (''.join(complementar))

def DnaToRna(complementar):     #Transkrypcja DNA do RNA
    m_RNA = []
    for nucleotide in complementar:   
        if nucleotide == 'A':
            m_RNA.append('U')
        elif nucleotide == 'T':
            m_RNA.append('A')
        elif nucleotide == 'C':
            m_RNA.append('G')
        elif nucleotide == 'G':
            m_RNA.append('C')
        else:
            pass

    print("Produkt transkrypcji:\n\n5'-",''.join(m_RNA), "-3'", "\n", file = out)
    return(m_RNA)
    
def Translation(m_RNA, k):      #Translacja RNA na sekwencję aminokwasową
    rna_len = len(m_RNA)
    a = int((rna_len+k)/3)
    aminoacids = []
    for i in range (0,a):
        codons = m_RNA[i*3+k:i*3+k+3]
        codon = ''.join(codons)
        
        if (codon == 'UUU') or (codon == 'UUC'):    
            aminoacids.append('Phe')
        elif (codon == 'UUA') or (codon == 'UUG') or (codon == 'CUU') or (codon == 'CUG') or (codon == 'CUC') or (codon == 'CUA'):
            aminoacids.append('Leu')
        elif (codon == 'AUU') or (codon == 'AUC') or (codon == 'AUA'):
            aminoacids.append('Ile')
        elif (codon == 'AUG'):
            aminoacids.append('Met')
        elif (codon == 'GUA') or (codon == 'GUU') or (codon == 'GUC') or (codon == 'GUG'):
            aminoacids.append('Val')
        elif (codon == 'UCU') or (codon == 'UCC') or (codon == 'UCG') or (codon == 'UCA'):
            aminoacids.append('Ser')
        elif (codon == 'CCU') or (codon == 'CCC') or (codon == 'CCG') or (codon == 'CCA'):
            aminoacids.append('Pro')
        elif (codon == 'ACU') or (codon == 'ACG') or (codon == 'ACC') or (codon == 'ACA'):
            aminoacids.append('Thr')
        elif (codon == 'GCU') or (codon == 'GCC') or (codon == 'GCA') or (codon == 'GCG'):
            aminoacids.append('Ala')
        elif (codon == 'CGU') or (codon == 'CGC') or (codon == 'CGA') or (codon == 'CGG') or (codon == 'AGA') or (codon == 'AGG'):
            aminoacids.append('Arg')
        elif (codon == 'GGU') or (codon == 'GGC') or (codon == 'GGA') or (codon == 'GGG'):
            aminoacids.append('Gly')
        elif (codon == 'UAU') or (codon == 'UAC'):
            aminoacids.append('Tyr')
        elif (codon == 'CAU') or (codon == 'CAC'):
            aminoacids.append('His')
        elif (codon == 'CAA') or (codon == 'CAG'):
            aminoacids.append('Gln')
        elif (codon == 'AAU') or (codon == 'AAC'):
            aminoacids.append('Asn')
        elif (codon == 'AAA') or (codon == 'AAG'):
            aminoacids.append('Lys')
        elif (codon == 'GAU') or (codon == 'GAC'):
            aminoacids.append('Asp')
        elif (codon == 'GAA') or (codon == 'GAG'):
            aminoacids.append('Glu')
        elif (codon == 'UGU') or (codon == 'UGC'):
            aminoacids.append('Cys')
        elif (codon == 'UGG'):
            aminoacids.append('Trp')
        elif (codon == 'AGU') or (codon == 'AGC'):
            aminoacids.append('Ser')
        elif (codon == 'AGA') or (codon == 'AGG'):
            aminoacids.append('Arg')
        elif (codon == 'UAA') or (codon == 'UAG') or (codon == 'UGA'):
            aminoacids.append('STOP') 
            break
    print(aminoacids,'\n',file=out)
    return(aminoacids)
        
"""-------------------WYWOŁANIE-FUNKCJI------------------------------------------"""    
   
dna=Sequence()
complementar = ComplementarSequence(dna)
m_RNA=DnaToRna(complementar)
print("Łańcuch aminokwasowy (startujący z pierwszej pozycji łańcucha) :\n", file = out)
Translation(m_RNA,0)
print("Łańcuch aminokwasowy (startujący z drugiej pozycji łańcucha) :\n", file = out)
Translation(m_RNA,1)
print("Łańcuch aminokwasowy (startujący z trzeciej pozycji łańcucha) :\n", file = out)
Translation(m_RNA,2)
out.close() 
 
"""----------------------ASSERTS-------------------------------------------------"""
print("\nAsserts :\n")
assert ComplementarSequence('C') == 'G' , 'Niewłasciwa zamiana nukleotydów!!!'
assert DnaToRna('ATACCG') == 'UAUGGC', 'Niewłasciwa transkrypcja!!!'
assert Translation(['A','G','U']) == ['Ser'], 'Niewłasciwa translacja!!!'



