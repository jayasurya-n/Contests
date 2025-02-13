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
        m = ii()
        arr = lii()
        
        nonzeros = []
        first = True
        for i in range(m):
            if(first or arr[i]!=0):
                nonzeros.append(arr[i])
                if(arr[i]==0):first = False
        
        n = len(nonzeros)
        suf_mex = [0]*n
        hash = [False]*(n+1)

        mex = 0
        for i in range(n-1,-1,-1):
            if(nonzeros[i]<=n):hash[nonzeros[i]] = True
            while(hash[mex]):mex+=1
            suf_mex[i] = mex

        ans = n
        if(first):return ans
        
        mini = 10**10
        for i in range(n-1):
            mini = min(mini,nonzeros[i])
            if(mini<suf_mex[i+1]):
                ans-=1
                break
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)