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
        n,k = lii()
        amin = ceil((sqrt(k**2+8*k+4)+k)/2)
        # print("amin",amin)
        if(amin>n):return [-1,-1]
        
        if(amin%2==1 or amin+1<=n):
            if(amin%2==0 and amin+1<=n):amin+=1
            b = 2
            if(amin-b>=k):return [amin,b]
            diff = k+b-amin
            amin+=diff
            if(amin>n):return [-1,-1]
            return [amin,b]
        return [-1,-1]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)