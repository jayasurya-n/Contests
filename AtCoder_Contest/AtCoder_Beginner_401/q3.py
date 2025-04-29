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
        n,k = lii()
        if(n<k):return 1
        mod = 10**9
        
        q = deque([1]*k)
        prev = k 
        curr = 0
        for i in range(k,n+1):
            curr = prev
            q.append(curr)
            prev+=curr-q.popleft()
            prev%=mod
        return curr
            

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)