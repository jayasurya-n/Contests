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
        arr = lii()
        
        csum = 0
        last = -1
        for i in range(n):
            csum+=arr[i]
            csum%=3
            if(csum==0):last = i
        
        if(last==-1):return yes
        if(last==n-1):return no
        
        hash = defaultdict(int)
        hash[0] = 1
        csum = 0

        for i in range(n):
            csum+=arr[i]
            csum%=3
            if(hash[csum]==0 and i>last):return yes
            hash[csum]+=1

        return no 
                
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)