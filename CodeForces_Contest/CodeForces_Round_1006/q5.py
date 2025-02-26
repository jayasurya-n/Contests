from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
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
        k = ii()
        if(k==0):
            print(1)
            print("0 0")
            return
        
        groups = []
        while k>0:
            s = int((1+sqrt(1+8*k))/2)
            while s*(s-1)//2>k:s-=1
            groups.append(s)
            k-=s*(s-1)//2
        
        n = sum(groups)
        print(n)
        
        x = 0
        gap = 10**4
        for i,s in enumerate(groups):
            y = i*gap
            for j in range(s):
                print(x+j,y)
            x+=s+1


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        # print(ans)