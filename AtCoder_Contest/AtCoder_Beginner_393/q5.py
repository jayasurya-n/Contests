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
        n,k = lii()
        arr = lii()
        
        m = max(arr)
        cnt = [0]*(m+1)
        mul = [0]*(m+1)
        gcd_ = [1]*(m+1)
        
        for num in arr:cnt[num]+=1
        for i in range(1,m+1):
            for j in range(i,m+1,i):
                mul[i]+=cnt[j]
                
        for i in range(1,m+1):
            if(mul[i]<k):continue
            for j in range(i,m+1,i):gcd_[j]=i
        
        for num in arr:print(gcd_[num])

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()