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
        n,c = lii()
        a = lii()
        cost = lii()
        
        vitamins = dict()
        for i in range(n):
            if(a[i] not in vitamins):
                vitamins[a[i]] = cost[i]
            else:
                vitamins[a[i]] = min(cost[i],vitamins[a[i]])
        
        vitamins = sorted(vitamins.items(),key=lambda x:x[1])
        ans = curr_cost = 0
        for i in range(len(vitamins)):
            curr_max = (i+1)*c
            curr_cost+=vitamins[i][1]
            ans = max(ans,curr_max-curr_cost)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)