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
        n,m,d = lii()
        grid = []
        mod = 998244353
        
        for _ in range(n):grid.append(si())
        grid.reverse()
        
        # dp[i][j][f]: no of ways to reach to (i,j) from level 0
        # given that 1+f holds are used in row i
        # trainsition: 
        # dp[i][j][0]+= sum(dp[i][j-d][1] to dp[i][j+d][1]) - dp[i][j][1] 
        # dp[i][j][f]+= sum(dp[i-1][j-d+1][f] to dp[i-1][j+d-1][f]) 
        # sum(dp[n-1][j][0])
        
        prev = [[0]*2 for _ in range(m)]
        prefix_prev = [[0]*2 for _ in range(m)]
        
        for i in range(n):
            curr = [[0]*2 for _ in range(m)]
            prefix_curr = [[0]*2 for _ in range(m)]
            for f in range(1,-1,-1):
                for j in range(m):
                    if(grid[i][j]=='#'):continue
                    ans = 0
                    if(i==0):ans+=1
                    
                    if(f==0):
                        r = min(m-1,j+d)
                        l = max(0,j-d)
                        ans+= prefix_curr[r][1]-(prefix_curr[l-1][1] if l>0 else 0)
                        ans-=curr[j][1]
                        ans%=mod
                        
                    if(i>0):
                        r = min(m-1,j+d-1)
                        l = max(0,j-d+1)
                        ans+= prefix_prev[r][0]-(prefix_prev[l-1][0] if l>0 else 0)
                        ans%=mod

                    prefix_curr[j][f] = curr[j][f] = ans
                    
                for j in range(1,m):
                    prefix_curr[j][f]+=prefix_curr[j-1][f]
                    prefix_curr[j][f]%=mod    
                
            prefix_prev = prefix_curr
            prev = curr
        
        ans = 0
        for j in range(m):
            ans+=curr[j][0]
            ans%=mod
        return ans
        
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)