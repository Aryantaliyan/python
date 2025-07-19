num=int(input("enter a number: "))
for i in range(1,num+1):
    for j in range((num)-i):
        print(" "*2,end="")
    for j in range((i*2)-1):
        print("* ",end="")
    print()
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""