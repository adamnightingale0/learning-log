def count_nucleotides(sequence):
    #counts numbers of nucleotides in a given sequence
    counts = {}
    for nt in sequence:
        if nt.isalpha():
            if nt.upper() in counts:
                counts[nt.upper()] += 1
            else:
                counts[nt.upper()] = 1
        else:
            counts["non-nucleotide"] = counts.get("non-nucleotide", 0) + 1
    return counts

sequence1 = "ATCG"
sequence2 = "ACTGTgtcGATGCTAG"
sequence3 = "ATCGAGGACA 5TCGATGC"

print(count_nucleotides(sequence1))  
print(count_nucleotides(sequence2))  
print(count_nucleotides(sequence3))  

def test(sequence):
    return sum(count_nucleotides(sequence).values()) == len(sequence)

print(test(sequence1)) 
print(test(sequence2))  
print(test(sequence3))  