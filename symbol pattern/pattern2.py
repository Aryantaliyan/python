rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print(f"{j+1} ",end="")
    print()

"""
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""