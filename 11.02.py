'''      *   4 spaces 
       *   *  3 spaces * + "" *(2*2-3)+* 
      *     *  2 spaces * + "" * (2*3-3)+*
     *       * 1 sapces * + "" *(2*4-3)+ *
     *********   i==5 *(2*5-1) '''

def hollow_pyramid(n):
    for i in range(1,n+1):
        space=" "*(n-i)  #""*5-1  space calucaltion for the first row
        if i==1:
            print(space+"*")
        elif i==n:  #last row 
            print("*"*(2*n-1))  #2*5-1->10-1->9 stars
        else:
             print(space + "*" + "*" * (2 * i - 3) + "*")
                   #middle rows->space+*+space+*

n=int(input("Enter the heigth:"))  #5
hollow_pyramid(n)   #function call


