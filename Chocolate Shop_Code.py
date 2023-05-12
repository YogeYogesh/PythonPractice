
#Chocolate Shop program
print("Hi, Welcome to Chocolate Shop")
dict1={"kitkat":500,"dairymilk":400,"munch":300,"milkybar":200}
userinput=input("Which Chocolate You Want")
if userinput in dict1:
    print("Yes, This Chocolate is Available in Shop")
    quantity=int(input("How Many Chocolate You Want: "))
    if dict1[userinput]>=quantity:
        print("Yes, This Quantity is Available and You Have 10% Discount")
        bill=quantity*50*1/100
        print("Amount",bill)
    else:
        print("This quantity is not available in Shop.")
        other=input("Do You Want Other Chocolate: ")
        if other=="yes":
            userinput=input("Which Chocolate You Want")
            if userinput in dict1:
                print("Yes, This Chocolate is Available in Shop")
                quantity=int(input("How Many Chocolate You Want: "))
                if dict1[userinput]>=quantity:
                    print("Yes, This Quantity is Available and You Have 10% Discount")
                    bill=quantity*50*1/100
                    print("Amount",bill)
                else:
                    print("Thank You Visit Again")
else:
    print("This Chocolate is not available in Shop.")
    other=input("Do you want other chocolate")
    if other=="yes":
            userinput=input("Which Chocolate You Want")
            if userinput in dict1:
                print("Yes, This Chocolate is Available in Shop")
                quantity=int(input("How Many Chocolate You Want: "))
                if dict1[userinput]>=quantity:
                    print("Yes, This Quantity is Available and You Have 10% Discount")
                    bill=quantity*50*1/100
                    print("Amount",bill,"Thank You Visit Again")
    else:
        print("Thank You Visit Again")


        
    
    
