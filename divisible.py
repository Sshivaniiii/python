#num=int(input("enter the number:"))
#if(num%7==0):
 #   print("it is divisible by 7")
#else:
 #   print("it is not divisible by 7")
a=int(input("enter first number:"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
if(a>b and a>c and a>d):
    print("a is largest")
elif(b>c and b>d and b>a):
    print("b is largest")
elif(c>a and c>d and c>b):
    print("c is largest")
else:
    print("d is largest")