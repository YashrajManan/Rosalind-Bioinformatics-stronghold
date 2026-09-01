codons = {
     "F": 2,
    "L": 6,
    "I": 3,
    "M": 1,
    "V": 4,
    "S": 6,
    "P": 4,
    "T": 4,
    "A": 4,
    "Y": 2,
    "H": 2,
    "Q": 2,
    "N": 2,
    "K": 2,
    "D": 2,
    "E": 2,
    "C": 2,
    "R": 6,
    "G": 4,
    "W": 1
}

STOP = 3 

with open("D:\Workspace\Python\ROSALIND-DSA\problem17data.txt", "r") as file:
    protein = file.readline().strip() 

answer = 1 
mod =1000000 

for amino_acid in protein: 
    answer = (answer* codons[amino_acid])%mod 
answer = (answer*STOP)%mod 

print(answer) 