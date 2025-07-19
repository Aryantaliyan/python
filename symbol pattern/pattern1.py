rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print(f"{i} ",end="")
    print()

"""
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""