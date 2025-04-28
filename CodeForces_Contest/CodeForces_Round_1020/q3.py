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
        a = lii()
        b = lii()
        
        sum = None
        for i in range(n):
            if(b[i]==-1):continue
            if(sum==None):sum = a[i]+b[i]
        
        if(sum==None):return k+1-(max(a)-min(a))
            
        for i in range(n):
            if(b[i]!=-1 and a[i]+b[i]!=sum):return 0
            new = sum-a[i]
            if(new<0 or new>k):return 0
        
        return 1
               
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)