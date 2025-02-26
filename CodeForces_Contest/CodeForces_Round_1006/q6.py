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
        n,k = lii()
        n-=1
        for i in range(n+1):
            if(power[n]-power[i]-power[n-i]):print(0,end=" ")
            else:print(k,end=" ")
        print()
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    N = 10**6+2
    power = [0]*N 
    for i in range(N):
        curr = i
        while curr and curr%2==0:
            power[i]+=1
            curr//=2
        power[i]+=power[i-1]
        
    for _ in range(ii()):
        ans = Solution().run()
        # print(*ans)