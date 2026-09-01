with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem5data.txt", "r") as file: 

    sequences = {}
    current_id =""
    for line in file: 
        line = line.strip() 
        if line.startswith(">"): 
            current_id = line[1:] 
            sequences[current_id] = ""
        else:
            sequences[current_id] += line  
    highest_gc = 0
    highest_id = "" 

    for seq_id, dna in sequences.items(): 
        gc = dna.count("G") + dna.count("C") 
        gc_percent = (gc/len(dna))*100 

        if gc_percent > highest_gc: 
            highest_gc = gc_percent
            highest_id = seq_id  

    print(highest_id)
    print(highest_gc)