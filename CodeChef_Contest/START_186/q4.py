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
        n,x,y = lii()
        arr = lii()

        r = 0
        while(r<n and arr[r]>y):r+=1


        def check(k):
            b = sorted(arr[:k+1],reverse=True)
            dp = [0]*(x+1)
            dp[x] = 1

            for s in range(x,-1,-1):
                if(dp[s]==0):continue
                for bi in b:
                    dp[s%bi] = 1
            return dp[y]
                    
        low,high = 0,r-1
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        
        print(r-low)
        for i in range(low,r):
            print(i+1,end=" ")
        print()


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()