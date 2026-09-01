with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem2data.txt", "r") as file: 
    dna = file.read().strip() 
    rna =[] 
    for ch in dna: 
        if ch == "T": 
            rna.append("U") 
        else: 
            rna.append(ch)
    rna_string = "".join(rna)
    print(rna_string)
