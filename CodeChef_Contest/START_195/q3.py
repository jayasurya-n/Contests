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
        
        arr.sort(reverse=True)
        psum = [0]*n
        for i in range(n):
            psum[i] = arr[i]+(psum[i-1] if i>0 else 0)

        ans = []
        for k in range(1,2*n+1):
            best = 0
            for length in range(min(k,n)+1):
                c2 = min(k-length,length)
                c1 = length-c2
                best = max(best,
                           (psum[length-1] if length>0 else 0)+c1*c2+(c2*(c2-1))//2)
            ans.append(best)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)