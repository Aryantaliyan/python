num=int(input("enter a number: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        if(i==1 or i==num):
            print("* ",end="")
        elif(j==1 or j==num ):
            print("* ",end="")
        else:
            print(" "*2,end="")
    print()

"""

* * * * *
*       *
*       *
*       *
* * * * *

"""