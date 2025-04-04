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
        arr = lii()
        mod = 998244353

        n = sum(arr)
        even = n//2
        odd = n-even
        
        ans = (fac[even]*fac[odd])%mod
        for c in arr:
            if(c==0):continue
            ans*=pow(fac[c],mod-2,mod)
            ans%=mod
        
        # dp = [0]*(odd+1)
        # dp[0] = 1
        
        # for c in arr:
        #     if(c==0):continue
        #     for csum in range(odd,c-1,-1):
        #         dp[csum] = (dp[csum]+dp[csum-c])%mod
        
        # ans*=dp[odd]
        # ans%=mod
        # return ans
        
        pos = [c for c in arr if c>0]
        # dp[i][csum] = no of ways to form csum using nums[0 to i]
        # transition: dp[i][csum] = dp[i-1][csum]+dp[i-1][csum-pos[i]]
        # base case: dp[i][0] = 1
        
        dp = [[0]*(odd+1) for _ in range(len(pos))]
        for i in range(len(pos)):dp[i][0] = 1        
        
        for i in range(len(pos)):
            for csum in range(1,odd+1):
                dp[i][csum]+=dp[i-1][csum]
                if(pos[i]<=csum):
                    dp[i][csum]+=dp[i-1][csum-pos[i]]
                    dp[i][csum]%=mod
        
        ans*=dp[len(pos)-1][odd]
        ans%=mod
        return ans
                
                    
if __name__ == "__main__":
    fac = factorial(n=5*(10**5)+5,mod=998244353)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)