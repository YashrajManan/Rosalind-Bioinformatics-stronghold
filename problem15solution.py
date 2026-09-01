with open ("D:\Workspace\Python\ROSALIND-DSA\problem15data.txt", "r") as file:
    k, N = map(int, file.read().split()) 

total = 2**k
p = 1/4 
q = 1 - p  

from math import comb 

answer = 0 
for i in range(N, total + 1):
    answer+= comb(total, i) * (p**i) * (q**(total-i)) 

print(round(answer, 3)) 


