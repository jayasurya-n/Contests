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
        n = ii()
        s = si()
        if(s=="AB"):return alice
        if(s=="BA"):return bob
        
        if s.count('B')==1 and s.count('A')>1:return alice
        if(s[n-1]=='B' and s.count('B')>1):return bob
        if(s[n-1]=='A' and s[0]=='A'):return alice
        if(s[n-1]=='A' and s[0]=='B' and s[n-2]=='B'):return bob
        if(s[n-1]=='A' and s[0]=='B' and s[n-2]=='A'):return alice
        return bob

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    alice,bob = "Alice","Bob"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)