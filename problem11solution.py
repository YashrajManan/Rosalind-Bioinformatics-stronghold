with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem11data.txt", "r") as file:
    n, m =map(int, file.readline().split())

ages = [0]*m 
ages[0] = 1

for month in range(2,n+1):
    newborns = sum(ages[1:])
    ages = [newborns] + ages[:-1]

print(sum(ages))


    