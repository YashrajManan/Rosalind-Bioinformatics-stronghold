with open("D:\Workspace\Python\ROSALIND-DSA\problem13data.txt", "r") as file: 
    data = file.read().split()
    a,b,c,d,e,f = map(int, data) 

    expected = ((2*a)*(1) + (2*b)*(1) + (2*c)*(1) + (2*d)*(3/4) + (2*e)*(1/2) + (2*f)*(0)) 

    print(expected)   
