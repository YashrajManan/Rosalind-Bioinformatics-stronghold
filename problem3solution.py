with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem3data.txt", "r") as file: 
    dna = file.read().strip() 

    reverse_complement = [] 

    for i in range(len(dna)-1, -1, -1):
        ch = dna[i] 
        if ch == "A": 
            reverse_complement.append("T") 
        elif ch =="T":
            reverse_complement.append("A") 
        elif ch == "C": 
            reverse_complement.append("G") 
        else: 
            reverse_complement.append("C") 
    print("".join(reverse_complement)) 