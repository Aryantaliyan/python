rows=int(input("enter no of rows: "))
for i in range(1,rows+1):
    for j in range((rows+1)-i):
        print(f"{(rows+1-i)-j} ",end="")
    print()
"""
5 4 3 2 1 
4 3 2 1
3 2 1
2 1
1

"""