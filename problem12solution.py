sequences = {} 
current_id = "" 
current_sequence = "" 

with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem12data.txt", "r") as file:
    for line in file: 
        line = line.strip()

        if line.startswith(">"): 

            if current_id: 
                sequences[current_id] = current_sequence

            current_id = line[1:] 
            current_sequence = ""  

        else: 
            current_sequence += line 

    if current_id: 
        sequences[current_id] = current_sequence

ids = list(sequences.keys())

for i in range(len(ids)): 

    for j in range(len(ids)):

        if i == j:
            continue

        s = sequences[ids[i]]
        t = sequences[ids[j]]

        if s[-3:] == t[:3]: 

            print(ids[i], ids[j])