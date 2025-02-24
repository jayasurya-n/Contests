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
        n = ii()
        arr = lii()
        
        prev = -n
        for i in range(n-2):
            if(arr[i]==0):continue
            if(arr[i]==1):
                if(i-prev==2):return no
                prev = i
        return yes

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)