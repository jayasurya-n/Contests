from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        sum = (n*(n+1))//2
        y = int(sum**0.5)
        if(y*y==sum):return [-1]
        
        arr = list(range(1,n+1))     
        arr[0] = 2
        arr[1] = 1
        
        for i in range(2,n+1):
            sum = (i*(i+1))//2
            x = int(sum**0.5)
            if(x*x==sum):
                # print(sum,i)
                arr[i-1],arr[i] = arr[i],arr[i-1]
        return arr


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(*
              ans)