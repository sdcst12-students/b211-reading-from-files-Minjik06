filename1='data02.csv'

file=open(filename1, "r")

fileData1=file.read()

sp2 = fileData1.split("\n")


print(sp2)




k=[]
for i in range(len(sp2)):
    k.extend(sp2[i].split(','))
print(k)



sto=[]
st=0
for i in range(int(len(k)/3)):
    sto.append(k[st])
    st+=3
print(sto)

sym=[]
sy=1
for i in range(int(len(k)/3)):
    sym.append(k[sy])
    sy+=3
print(sym)

pri=[]
pr=2
for i in range(int(len(k)/3)):
    pri.append(k[pr])
    pr+=3
print(pri)

a=str(input("Enter stock symbol: "))
if a in sym:
    k=sym.index(a)
    print(f"Price of the symbol is {pri[k]}")
else:
    print("no match found")
