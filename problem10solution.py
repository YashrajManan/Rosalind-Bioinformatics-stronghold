dna = []
current = ""

with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem10data.txt") as file:
    for line in file:
        line = line.strip()

        if line.startswith(">"):

            if current:
                dna.append(current)

            current = ""

        else:
            current += line

if current:
    dna.append(current)
   

profile = {
         "A": [],
         "C": [],
         "G": [],
         "T": []
             }        

consensus = ""

for col in range(len(dna[0])): 
    count = {"A": 0, "C": 0, "G": 0, "T": 0} 

    for row in range(len(dna)):   
        nucleotide = dna[row][col]
        count[nucleotide] += 1 

    profile["A"].append(count["A"])
    profile["T"].append(count["T"])
    profile["G"].append(count["G"])     
    profile["C"].append(count["C"])

    consensus += max("ACGT", key=count.get) 

print(consensus) 

for nucleotide in "ACGT":
    print(f"{nucleotide}:", *profile[nucleotide])