from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        x,y =  0,0
        xmin,ymin = 0,0
        for i in range(n):
            x1,y1 = list(map(int,input().strip().split()))
            if(i==0):xmin,ymin=x1,y1
            x+=x1
            y+=y1
        return 2*((m+x-xmin)+(m+y-ymin))

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)