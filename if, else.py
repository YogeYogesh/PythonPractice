#ODD or Even

number=int(input("enter the number"))
if(number%2==0):
    print("This is even number")
else:
    print("This is odd number")


#greatest number 


num1=int(input("enter the number"))
num2=int(input("enter the number"))
if(num1>num2):
    print("Number 1 is the greatest number")
else:
    print("Number 2 it the greatest number")


#positive value or negative value

number=int(input("Enter the value"))
if(number>0):
           print("The number is positive value")

else:
    print("The number is negative value")


#working days, absent days, total days

total=int(input("Enter the total days"))
working=int(input("Enter the working days"))
sum=(total/working)*100
if(sum>75):
    print("you are eligible for exam")
else:
    print("you are not eligible for exam")
