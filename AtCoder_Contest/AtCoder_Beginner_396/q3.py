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
        n,m = lii()
        B = lii()
        W = lii()
        
        B.sort(reverse=True)
        W.sort(reverse=True)
        
        i = 0
        csum = 0
        while(i<min(n,m)):
            if(B[i]>0 and W[i]>0):csum+=W[i]+B[i]
            else:break
            i+=1
        
        while(i<n and B[i]>0):
            csum+=B[i]
            i+=1
        
        while(i<n and i<m):
            if(W[i]+B[i]>=0):csum+=B[i]+W[i]
            else:break
            i+=1
        
        return csum

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)