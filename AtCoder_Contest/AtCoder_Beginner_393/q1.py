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
        s1,s2 = lsi()
        if(s1=="fine" and s2=="fine"):return 4
        elif(s1=="sick" and s2=="sick"):return 1
        elif(s1=="sick" and s2=="fine"):return 2
        elif(s1=="fine" and s2=="sick"):return 3
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)