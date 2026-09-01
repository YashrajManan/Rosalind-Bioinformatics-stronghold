
with open('/mnt/d/Workspace/Python/ROSALIND-DSA/problem9data.txt', 'r') as file:
    s = file.readline().strip()

    t = file.readline().strip()

positions = []

for i in range(len(s)-len(t)+1):

    substring = s[i:i+len(t)]

    if substring == t:

        positions.append(i+1)

print(*positions)