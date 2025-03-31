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
        n = ii()
        arr = lii()
        adj = [[] for _ in range(n)]
        
        for _ in range(n-1):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

        def get_mexp(g):
            for p in primes:
                if g%p!=0:return p
        
        def bfs(root):
            q = deque([(root,-1,0)])
            while q:
                u,parent,cur_gcd = q.popleft()
                cur_gcd = gcd(arr[u],cur_gcd) 
                val = get_mexp(cur_gcd)
                B[root]+=val
                for v in adj[u]:
                    if v==parent:continue
                    q.append((v,u,cur_gcd))
        
        B = [0]*n
        for root in range(n):bfs(root)
        return B


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    def sieve_primes(n):
        primes = [True]*(n+1)
        primes[0]=primes[1]=False
        for i in range(2,int(n**0.5)+1):
            if(primes[i]):  
                for j in range(i*i,n+1,i):primes[j] = False
        
        ans = []
        for i in range(int(n**0.5)+1):
            if(primes[i]):ans.append(i)      
        return ans
    
    primes = sieve_primes(n=2002)
    # print(primes)
    
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans) 