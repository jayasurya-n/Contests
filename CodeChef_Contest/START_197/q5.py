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
        n,k = lii()
        mod = 998244353
 
        if(2*k>n):return pow(k,n,mod)   

        # power[a][b] (k-a)**(n-b)
        powers = [[0]*(k+1) for _ in range(k+1)] 
        for a in range(0,k):
            val = powers[a][0] = pow(k-a,n,mod)
            mul = modinv(k-a,mod)
            for b in range(1,a+1):
                val = val*mul%mod
                powers[a][b] = val

                
        ans = 0
        sign = 1
        for i in range(1,k+1):
            cnt = 0
            for t in range(i+1):
                ways = nCr(n,t,fac,inv_fac,mod)
                ways = ways*nCr(i,t,fac,inv_fac,mod)%mod
                ways = ways*powers[i][t]%mod
                ways = ways*fac[t] % mod
                cnt=(cnt+ways)%mod
            
            cnt=cnt*nCr(k,i,fac,inv_fac,mod)%mod
            ans+=sign*cnt
            ans%=mod
            sign*=-1
        
        return ans
    
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    fac,inv_fac = factorial(10**4+1,998244353)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)