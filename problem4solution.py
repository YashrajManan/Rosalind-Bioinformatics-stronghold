with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem4data.txt", "r") as file: 
    n,k = map(int,file.read().split())
    prev1 = 1 
    prev2 = 1 

    if n<= 2: 
        print(1)

    else:
        for i in range(3,n+1):
            current = prev1 + k*prev2
            prev2 = prev1
            prev1 = current 

        print(prev1) 

