from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def sieve_primes(n):
    primes = [True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if(not primes[i]):continue  
        for j in range(i*i,n+1,i):primes[j]=False  
    return [i for i in range(2,n+1) if primes[i]]

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        
        arr.sort(reverse=True)
        csum = psum = ans = 0
        for i in range(n):
            csum+=arr[i]
            psum+=primes[i]
            if(csum>=psum):ans = i+1
            else:break
        return n-ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    primes = sieve_primes(n=6*10**6)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)