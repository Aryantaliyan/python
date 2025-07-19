num=int(input("enter a number: "))
for i in range(1,num+1):
    for j in range((num+1)-i):
        print(" "*2,end="")
    for j in range(i+(i-1)):
        print("* ",end="")
    print()
for i in range(1,num):
    for j in range(i+1):
        print(" "*2,end="")
    for j in range((num-i)+(num-i-1)):
        print("* ",end="")
    print()

"""
        *
      * * *
    * * * * *
  * * * * * * * 
* * * * * * * * *
  * * * * * * *
    * * * * * 
      * * * 
        *
"""