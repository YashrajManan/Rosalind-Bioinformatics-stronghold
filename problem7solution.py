with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem7data.txt", "r") as file: 
    k,m,n = map(int, file.readline().split()) 
    total = k+m+n 

    term1 = (m/total) * ((m-1)/(total-1)) * (1/4)

    term2 = ((m/total) * (n/(total-1)) + (n/total) * (m/(total-1))) * (1/2)

    term3 = (n/total) * ((n-1)/(total-1))

    recessive = term1 + term2 + term3

    p_dominant = 1 - recessive

    print(round(p_dominant, 5))

