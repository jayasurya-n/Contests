from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        ope = []
        val = []
        for _ in range(n):
            s = si().split()
            ope.append((s[0],s[2]))
            val.append((int(s[1]),int(s[3])))
        
        dir = [0]*(n+1)
        for i in range(n-1,-1,-1):
            if(ope[i][0]=='+' and ope[i][1]=='+'):dir[i] = dir[i+1]
            elif(ope[i][0]=='+' and ope[i][1]=='x'):dir[i] = 1
            elif(ope[i][0]=='x' and ope[i][1]=='+'):dir[i] = 0
            elif(val[i][0]>val[i][1]):dir[i] = 0
            elif(val[i][0]<val[i][1]):dir[i] = 1
            else:dir[i] = dir[i+1]
        
        ans = [1,1]
        for i in range(n):
            gained = 0
            if(ope[i][0]=='+'):gained+=val[i][0]
            else:gained+=ans[0]*(val[i][0]-1)
            
            if(ope[i][1]=='+'):gained+=val[i][1]
            else:gained+=ans[1]*(val[i][1]-1)

            ans[dir[i+1]]+=gained
        
        return ans[0]+ans[1]
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)