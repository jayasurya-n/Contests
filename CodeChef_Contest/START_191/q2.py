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
        x,y,z = lii()
        if(x==0):return yes 
        if(y==0):
            if(x==1):return yes if z>=1 else no
            if(x>1):return yes if z>=x-1 else no
        
        elif(y>=1):
            if(x==1):return yes if z>=1 else no
            if(x>1):return yes if z>=x else no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "Yes","No"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)