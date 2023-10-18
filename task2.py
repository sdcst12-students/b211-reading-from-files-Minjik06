"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

filename1='task02a.txt'

file=open(filename1, "r")

fileData1=file.read()

sp1 = fileData1.split("\n")

print(sp1)

dict1={}


for i in range(len(sp1)):
    while i%4!=0:
        if i ==0:
            dict1[f"{i+1}a"]=sp1[i]
            sp1.pop(0)
        elif i==1:
            dict1[f"{i+1}b"]=sp1[i]
            sp1.pop(0)
        elif i==2:
            dict1[f"{i+1}c"]=sp1[i]
            sp1.pop(0)
    if i==4:
        sp1.pop(0)
dict={dict1}
print(dict)



