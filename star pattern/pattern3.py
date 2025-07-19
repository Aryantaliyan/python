num=int(input("enter a number: "))
for i in range(1,num+1):
    # Print leading spaces
    for j in range(num-i):
        print(" "*2,end="")
    for j in range(i):
        print("* ",end="")
    print(" ")

"""
        *
      * *
    * * *
  * * * *
* * * * *

"""