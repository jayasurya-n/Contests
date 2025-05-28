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
        arr = []

        for _ in range(n):
            x,y = lii()
            arr.append((x,y))

        if(n==1):return 1

        def solve(arr,ind):
            xmin = ymin = 10**10
            xmax = ymax = 0
            for i in range(n):
                if(i==ind):continue
                xmin = min(xmin,arr[i][0])
                ymin = min(ymin,arr[i][1])

                xmax = max(xmax,arr[i][0])
                ymax = max(ymax,arr[i][1])
            
            xlen = xmax-xmin+1
            ylen = ymax-ymin+1
            area = xlen*ylen
            
            if(area==n-1):
                area = min(area+xlen,area+ylen)
            return area

        xsort = sorted(arr,key=lambda ele:ele[0]) 
        ysort = sorted(arr,key=lambda ele:ele[1])

        ans = min(solve(xsort,0),solve(xsort,n-1),
                  solve(ysort,0),solve(ysort,n-1))
        return ans


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)