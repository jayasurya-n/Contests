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

def sieve_primes(n):
    primes = [True]*(n+1)
    primes[0]=primes[1]=False
    for i in range(2,int(n**0.5)+1):
        if(primes[i]):  
            for j in range(i*i,n+1,i):primes[j] = False            
    
    ans = []
    for i in range(2,n+1):
        if(primes[i]):ans.append(i)
    return ans

class Solution:
    def run(self):
        n = ii()
        ans = 0
        for p in primes:
            if(p>n):break
            ans+=n//p
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    primes = sieve_primes(10**7+1)
    
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)