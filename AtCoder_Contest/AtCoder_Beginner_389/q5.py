from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,M = list(map(int,input().strip().split()))
        prices = list(map(int,input().strip().split()))
        
        prices.sort()  
        ans = 0 
        budget = M

        for p_i in prices:
            units = int((budget//p_i)**0.5)
            ans+=units
            budget-=(units**2)*p_i
            if budget<=0:break
        return ans
                
if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)