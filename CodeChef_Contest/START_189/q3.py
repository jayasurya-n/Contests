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
    primes[1] = False
    for i in range(2,int(n**0.5)+1):
        if(not primes[i]):continue  
        for j in range(i*i,n+1,i):primes[j]=False  
    return primes

class Solution:
    def run(self):
        n = ii()
        if n == 2:return [1,2]
        if n == 3:return [2,1,3]
        if n == 4:return [2,1,3,4]
        if n == 5:return [2,1,3,4,5]
        if n == 6:return [2,1,3,5,4,6]
        if n == 7:return [2,1,3,5,4,7,6]
        if n == 8:return [2,1,3,5,4,7,6,8]

        primes_bool = sieve_primes(n)
        primes = []
        composites = deque([])
        for i in range(1,n+1):
            if(primes_bool[i]):primes.append(i)
            else:composites.append(i)
        
        ans = []

        for p in primes:
            if(composites and composites[0]<p):
                ans.append(composites.popleft())
            
            ans.append(p)

            if(composites and composites[0]<p):
                ans.append(composites.popleft())
        
        while composites:
            ans.append(composites.popleft())
        
        ans[0],ans[1] = ans[1],ans[0]
        ans[:8] = [2,1,3,5,4,7,6,8]
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)