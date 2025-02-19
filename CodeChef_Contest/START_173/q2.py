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
        
        if(n==1):return [-1]
        hash = set()
        
        for num in arr:
            if(num in hash):return [1,num]
            hash.add(num)
        return [-1]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        if(len(ans)==2):
            print(ans[0])
            print(ans[1])
        else:
            print(ans[0])