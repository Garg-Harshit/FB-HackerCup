#    ____                       _   _                _     _ _   
#   / ___| __ _ _ __ __ _      | | | | __ _ _ __ ___| |__ (_) |_ 
#  | |  _ / _` | '__/ _` |_____| |_| |/ _` | '__/ __| '_ \| | __|
#  | |_| | (_| | | | (_| |_____|  _  | (_| | |  \__ \ | | | | |_ 
#   \____|\__,_|_|  \__, |     |_| |_|\__,_|_|  |___/_| |_|_|\__|
#                   |___/                                        

from typing import Counter
import sys
from collections import defaultdict as dd
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
def pr_n(*x):
    print(*x,end=" ")
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
def printing(num1,num2,num3,num4):
    for i in range(num1):
        for j in range(num2):
            k = (num1+num2-2)
            if ((not i) and (not j)):
                pr_n(num3-k)
            elif ((not i) and (j==(num2-1))):
                pr_n(num4-k)
            else:
                pr_n(1)
        pr()
def check(num1,num2,num3,num4,_):
    if (not ((num3<(num1+num2-1)) or (num4<(num1+num2-1)))):
        pr(f"Case #{_+1}: Possible")
        printing(num1,num2,num3,num4)
    else:
        pr(f"Case #{_+1}: Impossible")
if __name__ =="__main__":
    cou=inp()
    for _ in range(cou):
        num1,num2,num3,num4 = vinp()
        check(num1,num2,num3,num4,_)