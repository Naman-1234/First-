#This is my solution of this code this problem is available on Hackerrank platform
from collections import OrderedDict         
def merge_the_tools(string, k):
    x=""
    for i in range(0,len(string),k):
        x+=string[i:i+k]
        x+='- '
    l=list()
    l=x.split('-')
    for i in l:
        i="".join((OrderedDict.fromkeys(i)))
    x=" ".join(l)
    l=x.split()
    for i in l:
        print(i)

            
if __name__ == '__main__':
