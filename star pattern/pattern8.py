num=int(input("enter a number: "))
for i in range(1,num+1):
    for j in range(num-i):
        print(" "*2,end="")

    for j in range((i*2)-1):
        if((i==num) or (j==0) or (j==(i*2)-2)):
            print("* ",end="")
        else:
            print(" "*2,end="")
    print()

"""
        * 
      *   * 
    *       * 
  *           * 
* * * * * * * * *

"""