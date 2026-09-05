dna = "" 
with open ("/mnt/d/Workspace/python/ROSALIND-DSA/problem18data.txt", "r") as file: 
    for line in file:
        line = line.strip() 

        if not line.startswith(">"):
            dna += line

complement = {"A":"T",
              "T":"A",
              "G":"C",
              "C":"G"
              }

reverse_complement = "".join(complement[b] for b in reversed(dna))

genetic_code = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "STOP", "TAG": "STOP",
    "TGT": "C", "TGC": "C", "TGA": "STOP", "TGG": "W",

    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",

    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",

    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

proteins = set()

for sequence in (dna, reverse_complement):

    for frame in range(3):

        for i in range(frame, len(sequence) - 2, 3):

            if sequence[i:i + 3] == "ATG":

                protein = ""

                for j in range(i, len(sequence) - 2, 3):

                    codon = sequence[j:j + 3]

                    if genetic_code[codon] == "STOP":
                        proteins.add(protein)
                        break

                    protein += genetic_code[codon]


print(*proteins, sep="\n")