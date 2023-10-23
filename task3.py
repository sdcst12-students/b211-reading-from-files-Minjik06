#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
#from _typeshed import Self


class sum:
    def file(self):

        filename1='task03.txt'

        file=open(filename1, "r")

        fileData1=file.read()

        sp2 = fileData1.split("\n")

        print(sp2)
        return sp2

    def maxS(self):
        a=self.file()
        max=0
        total=0
        for i in range(len(a)):
            if a[i]!='':
                total+=int(a[i])
            elif a[i]=='':
                if total>max:
                    max=total
                    total=0
                total=0
        print()
        print(max)
        return max
    
    def __init__(self):
        self.maxS()

s=sum()

