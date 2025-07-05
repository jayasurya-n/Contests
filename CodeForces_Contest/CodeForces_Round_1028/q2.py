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
        p = lii()
        q = lii()
        mod = 998_244_353

        def prefix_max(arr):
            pmax = [0]*n
            curr = arr[0]
            for i in range(1,n):
                pmax[i] = pmax[i-1]
                if(curr<arr[i]):
                    pmax[i] = i
                    curr = arr[i]
            return pmax

        pmax = prefix_max(p) 
        qmax = prefix_max(q)

        ans = []
        for i in range(n):
            i1,j1 = pmax[i],i-pmax[i]
            i2,j2 = qmax[i],i-qmax[i]

            if(p[i1]>q[i2] or 
               (p[i1]==q[i2] and q[j1]>=p[j2])):
                curr = pow(2,p[i1],mod)+pow(2,q[j1],mod)
                ans.append(curr%mod)

            elif(p[i1]<q[i2] or 
                 (p[i1]==q[i2] and q[j1]<p[j2])):
                curr = pow(2,q[i2],mod)+pow(2,p[j2],mod)
                ans.append(curr%mod)
        
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)