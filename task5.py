"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""
class stock:
    def file(self):
        filename1='data02.csv'

        file=open(filename1, "r")

        fileData1=file.read()

        sp2 = fileData1.split("\n")
        return sp2

    def stockSp(self):
        sp2=self.file()
        k=[]
        for i in range(len(sp2)):
            k.extend(sp2[i].split(','))
        return k

    def st1(self):
        k=self.stockSp()
        sto=[]
        st=0
        for i in range(int(len(k)/3)):
            sto.append(k[st])
            st+=3
        return sto

    def sy1(self):
        k=self.stockSp()
        sym=[]
        sy=1
        for i in range(int(len(k)/3)):
            sym.append(k[sy])
            sy+=3
        return sym

    def pr1(self):
        k=self.stockSp()
        pri=[]
        pr=2
        for i in range(int(len(k)/3)):
            pri.append(k[pr])
            pr+=3
        return pri

    def __init__(self):
        a=str(input("Enter stock symbol: "))
        s=self.sy1()
        p=self.pr1()
        count=0
        if a in s:
            k=s.index(a)
            print(f"Price of the symbol is {p[k]}")
        else:                
            for i in range(len(s)):
                if a in s[i]:
                    count+=1
            if count==0:
                print("no match found")
            else:
                print(f"There are {count} stocks with that symbol")

s=stock()