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
def lsinp():
    return list(input())
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
        a=inp()
        array=[]
        for i in range(a):
            array.append(lsinp())
        f=sys.maxsize
        co,key,hash_map=0,0,dd(int)
        for i in range(a):
            counter_temp=0
            temp=True
            for j in range(a):
                if array[i][j]=='.':
                    counter_temp+=1
                    key=j
                elif array[i][j]=='O':
                    temp=False
                    break
            if temp:
                z=False
                if f>counter_temp:
                    f=counter_temp
                    co=1
                    z=True
                elif f==counter_temp:
                    co+=1
                    z=True
                if z and f==1:
                    hash_map[key]+=1
        for i in range(a):
            if hash_map[i]==0:
                counter_temp = 0
                temp = 1
                for j in range(a):
                    if array[j][i]=='.':
                        counter_temp+=1
                    elif array[j][i]=='O':
                        temp=0
                        break
                if temp:
                    z=False
                    if f>counter_temp:
                        f=counter_temp
                        co=1
                        z=True
                    elif f==counter_temp:
                        co+=1
                        z=True
        if f!=sys.maxsize:
            pr(f"Case #{_+1}: {f} {co}")
        else:
            pr(f"Case #{_+1}: Impossible")