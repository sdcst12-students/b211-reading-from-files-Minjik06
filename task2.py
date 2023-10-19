"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

filename1='task02a.txt'

file=open(filename1, "r")

fileData1=file.read()

sp2 = fileData1.split("\n")

a=len(sp2)-1
for i in range(len(sp2)):
    if sp2[a-i]=='':
        sp2.pop(a-i)
print(sp2)

dict=[]
dict1=[]

count=0
for i in range(len(sp2)):
    count+=1
    dict1.append(int(sp2[i]))
    if count==3:
        count=0
        dict.append(dict1)
        dict1=[]
print(dict)

for i in range(len(dict)):
    dict[i].sort()
    """if int(dict[i][0])>int(dict[i][1]):
        a=int(dict[i][0])
        dict[i][0]=int(dict[i][1])
        dict[i][1]=a

    if int(dict[i][0])>int(dict[i][2]):
        a=int(dict[i][0])
        dict[i][0]=int(dict[i][2])
        dict[i][2]=a

    if int(dict[i][1])>int(dict[i][2]):
        a=int(dict[i][1])
        dict[i][1]=int(dict[i][2])
        dict[i][2]=a"""

print(dict)


#print(dict)

"""if count==3:
        count=0
        dict.append(dict1)
        for p in range(3):
            dict1.pop(0)"""

"""
split into groups of 4 elements
only use the first 3 to check for a triple
el 0, 1, 2, 3 - > append to list(list of 4 things)

data= [
    [62,46,43,0],
    [6,25,25,0]
]
"""














"""sp2=sp1
a=len(sp2)-1
for i in range(len(sp2)):
    if sp2[a-i]=='':
        sp2.pop(a-i)
print(sp2)

for j in range(len(sp1)/4):
    while sp1[j]!='':
        sp1[j]"""





"""a=len(sp1)-1
for i in range(len(sp1)):
    if sp1[a-i]=='':
        sp1.pop(a-i)
print(sp1)"""









"""for i in range(4):
    while i%4!=0:
        if i ==0:
            dict1[f"{i+1}a"]=sp1[i]
        elif i==1:
            dict1[f"{i+1}b"]=sp1[i]
        elif i==2:
            dict1[f"{i+1}c"]=sp1[i]
    if i==4:
        for j in range(4):
            dict.pop(j)"""


