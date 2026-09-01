import requests 

with open('D:/Workspace/Python/ROSALIND-DSA/problem16data.txt', 'r') as file: 
    ids = file.read().split() 

for protein_ids in ids:
    accession = protein_ids.split("_")[0]

    url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta"
    response = requests.get(url)

    lines = response.text.splitlines()
    sequence = "".join(lines[1:])
    positions = [] 

    for i in range(len(sequence)-3):
        if (sequence[i] == "N" and sequence[i+1] != "P"and sequence[i+2] in ["S", "T"] and sequence[i+3] != "P"):
            positions.append(i+1) 

    if positions:
        print(protein_ids)
        print(*positions)