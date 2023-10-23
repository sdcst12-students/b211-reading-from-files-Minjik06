"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math
class pytha:
    numOpyta=0
    
    def file(self):
        a=str(input('task02a.txt or task02b.txt or task02c.txt :'))
        filename1=a

        file=open(filename1, "r")

        fileData1=file.read()

        sp2 = fileData1.split("\n")
        return sp2

    def sp(self):
        p=self.file()
        a=len(p)-1
        for i in range(len(p)):
            if p[a-i]=='':
                p.pop(a-i)
        print(p)
        return p

    def spli(self):
        k=self.sp()
        dict=[]
        dict1=[]

        count=0
        for i in range(len(k)):
            count+=1
            dict1.append(int(k[i]))
            if count==3:
                count=0
                dict.append(dict1)
                dict1=[]
        print(dict)

        for i in range(len(dict)):
            dict[i].sort()
        print(dict)
        return dict
    
    def findPy(self):
        dict1=self.spli()
        pytha=[]
        for i in range(len(dict1)):
            if math.pow(dict1[i][2],2)==math.pow(dict1[i][0],2)+math.pow(dict1[i][1],2):
                pytha.append(dict1[i])
        print()
        print(pytha)
        print(len(pytha))
        self.numOpyta==len(pytha)
        return len(pytha)

    def __init__(self):
        self.findPy()

    
p=pytha()



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




"""def file(self, filen):
        filename1=filen

        file=open(filename1, "r")

        fileData1=file.read()

        sp2 = fileData1.split("\n")
        return sp2

    def sp(self):
        a=len(sp2)-1
        for i in range(len(sp2)):
            if sp2[a-i]=='':
                sp2.pop(a-i)
        print(sp2)
        return sp2

    def spli(self):
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
        print(dict)
    
    def findPy(self):
        pytha=[]
        for i in range(len(dict)):
            if math.pow(dict[i][2],2)==math.pow(dict[i][0],2)+math.pow(dict[i][1],2):
                pytha.append(dict[i])
        print()
        print(len(pytha))
        return len(pytha)"""









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


