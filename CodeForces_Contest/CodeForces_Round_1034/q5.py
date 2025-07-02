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

        hash = [0]*(n+1)
        for num in arr:hash[num]+=1

        mex = 0
        while hash[mex]>0:mex+=1

        ans = [0]*(n+2)
        extra = cnt = 0
        for num in range(mex+1):
            cnt+=hash[num]
            left = hash[num]
            right = left+extra+n-cnt
            extra+=hash[num]-1
            ans[left]+=1
            ans[right+1]-=1
        
        for i in range(1,n+2):
            ans[i]+=ans[i-1]
        
        return ans[:n+1]


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)