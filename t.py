filename1='task04.txt'

file=open(filename1, "r")

fileData1=file.read()

sp2 = fileData1.split("\n")

print(sp2)
    

lev=[]
lev.append(sp2[1-1])
print(lev)
print()
lev1=lev[0]
print(lev1)
print(len(lev1))
            
