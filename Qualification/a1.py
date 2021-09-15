#    ____                       _   _                _     _ _   
#   / ___| __ _ _ __ __ _      | | | | __ _ _ __ ___| |__ (_) |_ 
#  | |  _ / _` | '__/ _` |_____| |_| |/ _` | '__/ __| '_ \| | __|
#  | |_| | (_| | | | (_| |_____|  _  | (_| | |  \__ \ | | | | |_ 
#   \____|\__,_|_|  \__, |     |_| |_|\__,_|_|  |___/_| |_|_|\__|
#                   |___/                                        

from typing import Counter
import sys
from collections import defaultdict
from math import *

def vinp():
    return map(int,input().split())
def linp():
    return list(map(int,input().split()))
def sinp():
    return input()
def inp():
    return int(input())
def mod(f):
    return f % 1000000007
def pr(*x):
    print(*x)
def finp():
    f=open("input.txt","r")
    f=f.read().split("\n")
    return f
def finp():
    f=open("input.txt","r")
    f=f.read().split("\n")
    return f
def fout():
    return open("output.txt","w")
def fpr(f,x):
    f.write(x+"\n")
def csort(c):
    sorted(c.items(), key=lambda pair: pair[1], reverse=True)
def indc(l,n):
    c={}
    for i in range(n):
        c[l[i]]=c.get(l[i],[])+[i+1]
    return c

if __name__ =="__main__":
    cou=inp()
    for _ in range(cou):
        s=sinp()
        le=len(s)
        d=defaultdict(int)
        c=0
        for i in s:
            if i in ['A','E','I','O','U']:
                c+=1
            d[i]+=1
        ma=min((le-c)*2+c,(2*c)+(le-c))
        for i in s:
            if i in ['A','E','I','O','U']:
                l=c-d[i]
                r=le-c
            else:
                l=le-c-d[i]
                r=c
            ma=min(l*2 +r,ma)
        pr(f"Case #{_+1}: {ma}")
