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
        n,x = lii()
        dodging = lii()
        parrying = lii()

        suffix = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i] = max(suffix[i+1],dodging[i])
        
        ans = 0
        for i in range(n):
            if(x-ans>=parrying[i] and x-ans-1>=suffix[i+1]):
                ans+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)