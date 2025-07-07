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
        arr = lii()
        
        pre = [0]*n
        if(arr[0]>0):pre[0] = arr[0]
        
        for i in range(1,n):
            pre[i] = pre[i-1]
            if(arr[i]>0):pre[i]+=arr[i]  
        
        suf = [0]*n
        if(arr[-1]<0):suf[-1] = -arr[-1]
        
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1]
            if(arr[i]<0):suf[i]-=arr[i]
        
        ans = 0
        for i in range(n):
            ans = max(ans,pre[i]+suf[i])
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)