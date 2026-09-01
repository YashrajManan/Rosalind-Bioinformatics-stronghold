with open("/mnt/d/Workspace/Python/ROSALIND-DSA/rosalind_dna.txt", "r") as file:
    dna = file.read().strip()

freq = {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0
}

for ch in dna:
    freq[ch] += 1

print(freq["A"], freq["C"], freq["G"], freq["T"])
