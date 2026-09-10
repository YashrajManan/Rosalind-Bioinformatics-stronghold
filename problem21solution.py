with open("/mnt/d/Workspace/python/ROSALIND-DSA/problem21data.txt", "r") as file:
    dna = "" 
    for line in file: 
        line = line.strip() 

        if not line.startswith(">"):
            dna+=line 

def reverse_complement(sequence): 
    complement = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"
    } 

    result = "" 

    for base in sequence:
        result+=complement[base] 
    return result[::-1] 

for i in range(len(dna)): 
    for length in range(4,13):
        if i + length <= len(dna):
            substring = dna[i:i + length]
            if substring == reverse_complement(substring):
                print(i + 1, length)
