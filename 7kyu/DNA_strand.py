def DNA_strand(dna):
    """
    Input: String -> String
    produces the complementary DNA side. In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
    """
    complement = ''
    for element in dna:
        if element == 'A':
            complement += 'T'
        elif element == 'T':
            complement += 'A'
        elif element == 'C':
            complement += 'G'
        else:
            complement += 'C'
    
    return complement

#Test
print("Expected result: TTTT")
print("Actual result:", DNA_strand('AAAA'))
print("Expected result: TAACG")
print("Actual result:", DNA_strand('ATTGC'))
print("Expected result: CATA")
print("Actual result:", DNA_strand('GTAT'))