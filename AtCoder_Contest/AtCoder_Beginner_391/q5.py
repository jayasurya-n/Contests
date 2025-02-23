from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        p = ii()
        s = si()
        
        # dp[k][i][0]: minimum changes require to flip A^k(i)
        # dp[k][i][1]: value of A^k(i)
        # need to find dp[n][1]
        
        n = 3**p
        dp = [[] for _ in range(p+1)]
        for i in range(n):dp[0].append([1,s[i]]) 
        
        for k in range(1,p+1):
            for i in range(0,3**(p-k)):
                cnt1,val1 = dp[k-1][3*i]  
                cnt2,val2 = dp[k-1][3*i+1]
                cnt3,val3 = dp[k-1][3*i+2]  
                
                ans = None
                if(val1==val2 and val1==val3):
                    ans = [cnt1+cnt2+cnt3 - max(cnt1,cnt2,cnt3),val1]
                elif(val1==val2):ans = [min(cnt1,cnt2),val1]
                elif(val1==val3):ans = [min(cnt1,cnt3),val1]
                elif(val2==val3):ans = [min(cnt2,cnt3),val2]
                dp[k].append(ans)
        
        return dp[p][0][0]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)