#First_Last6

list1=[]
range1=int(input("Enter the Range Value"))
for i in range (range1):
    user_input=int(input("Enter the Range"))
    list1.append(user_input)
print(list1)
if list1[0]==6 or list1[-1]==6:
    print("True")
else:
    print("False")


#Same_First_Last
list1=[]
range1=int(input("Enter the Range Value"))
for i in range (range1):
    user_input=int(input("Enter the Range"))
    list1.append(user_input)
print(list1)
if list1[0]==list1[-1]:
    print("True")
else:
    print("False")

#Common_End_(First element equal or last element equal)
list1=[]
range1=int(input("Enter the Range Value"))
for i in range (range1):
    user_input=int(input("Enter the Range"))
    list1.append(user_input)
print(list1)
list2=[]
range1=int(input("Enter the Range Value"))
for i in range (range1):
    user_input=int(input("Enter the Range"))
    list2.append(user_input)
print(list2)
if list1[0]==list2[0] or list1[-1]==list2[-1]:
    print("True")
else:
    print("False")





