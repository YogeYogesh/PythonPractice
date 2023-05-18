#Convert Two List into dictionary

a=[1, 2, 3, 4, 5]
b=["a", "b", "c", "d", "e"]
dict1={}
for i in range(len(a)):
    key=a[i]
    dict1[key]=b[i]
print(dict1)

#Marks above 35

n=int(input("Enter the Number of Students: "))
dict1={}
for i in range(n):
    roll=int(input("Enter the Roll No.: "))
    name=input("Enter the Name: ")
    marks=int(input("Enter the Marks: "))
    if marks>35:
        dict1[roll]=[name,marks]
print(dict1)

#Vowels count in Sentence

dict1={}
sentence=input("Enter the Sentence: ")
count=0
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
for i in range(len(sentence)):
    key="a"
    if sentence [i]=="a":
        count+=1
    dict1[key]=count
    key="A"
    if sentence[i]=="A":
        count1+=1
    dict1[key]=count1
    key="e"
    if sentence [i]=="e":
        count2+=1
    dict1[key]=count2
    key="E"
    if sentence[i]=="E":
        count3+=1
    dict1[key]=count3
    key="i"
    if sentence [i]=="i":
        count4+=1
    dict1[key]=count4
    key="I"
    if sentence[i]=="I":
        count5+=1
    dict1[key]=count5
    key="o"
    if sentence [i]=="o":
        count6+=1
    dict1[key]=count6
    key="O"
    if sentence[i]=="O":
        count7+=1
    dict1[key]=count7
    key="u"
    if sentence [i]=="u":
        count8+=1
    dict1[key]=count8
    key="U"
    if sentence[i]=="U":
        count9+=1
    dict1[key]=count9
print(dict1)
    
    
#Counting the numbers

num1=[1, 1, 2, 3, 4, 4, 4, 5, 6, 6]
dict1={}
count=0
for i in range(len(num1)):
    num=num1[i]
    count=num1.count(num1[i])
    dict1[num]=count
print(dict1)
