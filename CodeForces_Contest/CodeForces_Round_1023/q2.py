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
        arr = lii()
        
        maxi = max(arr)
        mini = min(arr)
        if(maxi-mini-1>k or (maxi-mini-1==k and arr.count(maxi)>1)):
            print("Jerry")
            return
            
        if(sum(arr)%2):print("Tom")
        else:print("Jerry") 

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()