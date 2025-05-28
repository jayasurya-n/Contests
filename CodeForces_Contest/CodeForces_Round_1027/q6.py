from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        x,y,k = lii()
        if x==y:return 0

        g = gcd(x,y)
        x//=g
        y//=g

        def get_min_factors(x):
            divs = []
            for i in range(1,int(sqrt(x))+1):
                if(x%i==0):
                    divs.append(i)
                    if(i*i!=x):divs.append(x//i)
            
            n = len(divs)
            divs.sort()
            dp = [100]*n
            # dp[i]: min factors not exceeding k to decompose i
            # for j in range(i):dp[i] = min(dp[i],dp[j]+1)
            
            dp[0] = 0
            for i in range(1,n):
                for j in range(i):
                    if(divs[i]%divs[j]==0 and divs[i]//divs[j]<=k): 
                        dp[i] = min(dp[i],dp[j]+1)
            return dp[n-1] if dp[n-1]!=100 else -1
                            
        ans1 = get_min_factors(x)
        ans2 = get_min_factors(y)
        if(ans1==-1 or ans2==-1):return -1
        return ans1+ans2

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)