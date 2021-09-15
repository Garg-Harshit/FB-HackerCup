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
from bisect import *
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
def r1(x_list,o_list,fun3,k):
    if s[k]=="O":
        return mod(x_list[bisect_right(x_list,fun3)-1])
    elif s[k]=="X":
        return mod(o_list[bisect_right(o_list,fun3)-1])
def r2(x_list,o_list,pos,leng):
    final_count = 0
    temp = [0]
    for i in range(1,leng):
        k = pos[i]-1
        temp.append(mod(temp[-1] + r1(x_list,o_list,pos[i],k)))
        final_count = mod(final_count + mod(temp[i]*(pos[i+1] - pos[i])))
    return final_count
if __name__ =="__main__":
    cou=inp()
    for _ in range(cou):
        n = inp()
        s = sinp()
        temp_list , x_list , o_list , leng = [] , [] , [] , 0
        pre = -1
        for i in range(n):
            if s[i] == "O":
                o_list.append(i+1)
                if pre==1 or pre==-1:
                    temp_list.append(i+1)
                    leng+=1
                pre = 0
            elif s[i] == "X":
                x_list.append(i+1)
                if (not pre) or pre==-1:
                    temp_list.append(i+1)
                    leng+=1
                pre = 1
        temp_list.append(n+1)
        pr(f"Case #{_+1}:",r2(x_list,o_list,temp_list,leng))