dna = []
current = ""

with open("D:\Workspace\Python\ROSALIND-DSA\problem14data.txt", "r") as file:

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


# Use the shortest sequence as our base
base = min(dna, key=len)


# Try substrings from longest to shortest
for length in range(len(base), 0, -1):

    for i in range(len(base) - length + 1):

        substring = base[i:i + length]

        # Check whether substring exists in every DNA sequence
        if all(substring in sequence for sequence in dna):

            print(substring)
            exit()