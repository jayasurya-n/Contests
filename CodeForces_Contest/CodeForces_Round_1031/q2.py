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
        w,h,a,b = lii()
        x1,y1,x2,y2 = lii()

        if(min(x1+a,x2+a)<=max(x1,x2) and min(y1+b,y2+b)<=max(y1,y2)):
            if(abs(x1-x2)%a==0 or abs(y1-y2)%b==0):return yes
            return no

        if(min(x1+a,x2+a)>max(x1,x2)):
            return yes if abs(y1-y2)%b==0 else no

        if(min(y1+b,y2+b)>max(y1,y2)):
            return yes if abs(x1-x2)%a==0 else no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)