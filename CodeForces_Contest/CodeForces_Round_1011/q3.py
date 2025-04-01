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
        x,y = lii()
        if(x&y)==0:return 0
        if(x==y):return -1
        
        return 2**50-max(x,y)
        
        # dp[i][c1][c2], min k value formed using bits 0 to i-1
        # such that c1,c2 are carry for x+k, y+k at ith position 
        # trainsition: dp[i+1][nc1][nc2] = min(dp[i+1][nc1][nc2],newk)
        
        # L = 60
        # dp = [[[None for _ in range(2)] for _ in range(2)] for _ in range(L+1)]
        # dp[0][0][0] = 0
        
        # for i in range(L):
        #     digx = (x>>i)&1
        #     digy = (y>>i)&1
        #     for c1 in range(2):
        #         for c2 in range(2):
        #             if(dp[i][c1][c2]==None):continue
        #             for k in range(2):
        #                 s1,s2 = digx+k+c1,digy+k+c2
        #                 nc1,nc2 = s1>>1,s2>>1
        #                 if(s1&1==1 and s2&1==1):continue
                        
        #                 newk = dp[i][c1][c2]|(k<<i)
                        
        #                 if(dp[i+1][nc1][nc2]==None):dp[i+1][nc1][nc2] = newk
        #                 else:dp[i+1][nc1][nc2] = min(newk,dp[i+1][nc1][nc2])
        
        # ans = dp[L][0][0]
        # if ans>10**18 or ans==None:return -1
        # return ans
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)