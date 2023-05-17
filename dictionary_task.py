Convert Two List into dictionary

a=[1, 2, 3, 4, 5]
b=["a", "b", "c", "d", "e"]
dict1={}
for i in range(len(a)):
    key=a[i]
    dict1[key]=b[i]
print(dict1)

Marks above 35

n=int(input("Enter the Number of Students: "))
dict1={}
for i in range(n):
    roll=int(input("Enter the Roll No.: "))
    name=input("Enter the Name: ")
    marks=int(input("Enter the Marks: "))
    if marks>35:
        dict1[roll]=[name,marks]
print(dict1)

Vowels count in Sentence

str1=input("Enter the Sentence")
str1_lower=str1.lower()
vowels="aeiouAEIOU"
count=0
for i in str1_lower:
    if i in vowels:
        count=count+1
print(count)







