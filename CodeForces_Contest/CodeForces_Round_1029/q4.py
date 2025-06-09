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

        n1,n2 = arr[0],arr[1]
        if((2*n1-n2)%(n+1)!=0):return no
        y = (2*n1-n2)//(n+1)
        x = n2-n1+y
        if(x<0 or y<0):return no

        for i in range(1,n):
            if(arr[i]-arr[i-1]!=x-y):return no
        return yes

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)