from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        r = int(input().strip())
        ans = 0
        for x in range(r):
            temp = 4*r*r-(4*x*x+4*x+1)
            ans+=floor((sqrt(temp)-1)/2)
        return 4*ans+1
            
                
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