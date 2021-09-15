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
mod = lambda x: (x % 1000000007)
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
        l = inp()
        s = sinp()
        k = ""
        f = 0
        pr(l,len(s))
        tar = [["O",-1,-1,"X"]]
        for j in range(l):
            i = s[j]
            if i == "O":
                if k == "X":
                    tar.append([k,p,j,i])
                    f+=1
                k = "O"
                p = j
            if i == "X":
                if k == "O":
                    tar.append([k,p,j,i])
                    f+=1
                k = "X"
                p = j
        tar.append(["O",l,l,"X"])
        # if len(tar) > 2:
        #     # for i in range(1,len(tar)+1):
        #     #     for j in range(len(tar)-i):
        #     #         tar[j]
        #     #         tar[j]
        #     pr(tar)
        #     pass
        # elif len(tar) == 1:
        #     pr(f"Case #{_+1}:",(tar[0][1]+1)*(l-tar[0][2]))
        # else:
        #     pr(f"Case #{_+1}: 0")
        final_count = 0
        for i in range(f):
            for j in range(1,(f-i)+1):
                fx , lx= False , False
                p , vmi , vmx , n = 0 , tar[j][1] , tar[j+i][2] , 0
                if tar[j][0] == "X":
                    fx = True
                if tar[j+i][3] == "X":
                    lx = True
                if fx:
                    if tar[j-1][0] == "O":
                        p = tar[j-1][1]
                    else:
                        p = tar[j-1][2]
                else:
                    if tar[j-1][0] == "X":
                        p = tar[j-1][1]
                    else:
                        p = tar[j-1][2]
                if lx:
                    if tar[j+i+1][0] == "O":
                        n = tar[j+i+1][1]
                    else:
                        n = tar[j+i+1][2]
                else:
                    if tar[j+i+1][0] == "X":
                        n = tar[j+i+1][1]
                    else:
                        n = tar[j+i+1][2]
                # if i==1:
                #     pr(p,n)
                #     pr((vmi-p)*(n-vmx))
                final_count += ((i+1)*(vmi-p)*(n-vmx))% 1000000007
                final_count = (final_count % 1000000007)
        pr(f"Case #{_+1}:",final_count)

    # {0 1 2 3 (4} 5 {6) 7}  8  9           = 10 * 1
    # 0 1 2 3  4 {5  6 (7} {8) 9}          = 6  * 1
    # {0 1 2 3 (4} 5  6  7 { 8) 9}          = 10 * 2