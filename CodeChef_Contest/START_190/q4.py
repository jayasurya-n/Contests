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
        n,q = lii()
        arr = lii()

        ans = 0
        for i in range(n-1):
            ans+=min(arr[i],arr[i+1])

        for _ in range(q):
            ind,x = lii()
            ind-=1
            if(ind>0):
                ans-=min(arr[ind-1],arr[ind])
                ans+=min(arr[ind-1],x)
            if(ind+1<n):
                ans-=min(arr[ind+1],arr[ind])
                ans+=min(arr[ind+1],x)
            
            arr[ind] = x
            print(ans)
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()