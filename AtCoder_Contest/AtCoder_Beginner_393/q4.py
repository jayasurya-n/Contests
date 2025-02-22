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
        s = si()
        
        ones = []
        for i,ch in enumerate(s):
            if(ch=='1'):ones.append(i)
        
        med = len(ones)//2
        start = ones[med]-med
        
        ans = 0
        for i,pos in enumerate(ones):
            ans+=abs(pos-(start+i))
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)