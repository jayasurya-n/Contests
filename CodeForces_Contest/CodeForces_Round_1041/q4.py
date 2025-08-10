import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

def factorial(n,mod):
    fac = [1]*(n+1)
    for i in range(1,n+1):
        fac[i] = (fac[i-1]*i)%mod
    
    inv_fac = [1]*(n+1)
    inv_fac[n] = modinv(fac[n],mod)
    for i in range(n,0,-1):
        inv_fac[i-1] = (inv_fac[i]*i)%mod

    return fac,inv_fac

def nCr(n,r,fac,inv_fac,mod):
    if(n<r or n<0 or r<0):return 0
    return ((fac[n]*inv_fac[r])%mod * inv_fac[n-r])%mod

class Solution:
    def run(self):
        n,m = lii()
        adj = [[] for _ in range(n)]

        for _ in range(m):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        if(m>=n):return 0
        
        non_leafs = 0 
        ans = 1
        for u in range(n):
            if(len(adj[u])>1):
                cnt = 0
                for v in adj[u]:
                    if(len(adj[v])>1):cnt+=1
                if(cnt>2):return 0

                leafs = len(adj[u])-cnt
                ans = ans*fac[leafs]%mod
                non_leafs+=1

        if(non_leafs<=1):return ans*2%mod
        return ans*4%mod

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    mod = 10**9+7
    fac,_ = factorial(2*10**5+1,mod)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)