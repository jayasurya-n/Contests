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
        n,j,k = lii()
        arr = lii()
        j-=1

        less = great = 0
        for i in range(n):
            if(i==j):continue
            if(arr[i]<=arr[j]):less+=1
            else:great+=1
        
        eleminated = less+max(great-1,0)
        return yes if (n-k)<=eleminated else no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)