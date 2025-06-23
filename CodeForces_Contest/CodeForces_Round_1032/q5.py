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
        l,r = lsi()
        n = len(l)

        if(l==r):return 2*n

        def solve(i,tl,tr):
            if(i==len(l)):return 0

            upper = int(r[i]) if tr else 9
            lower = int(l[i]) if tl else 0

            if(upper-lower>=2):return 0
            if(upper==lower):
                return (int(l[i])==lower)+(int(r[i])==upper)+solve(i+1,tl,tr)
            
            return min((lower==int(l[i]))+(lower==int(r[i]))+solve(i+1,tl,0),
                         (upper==int(l[i]))+(upper==int(r[i]))+solve(i+1,0,tr))

        return solve(0,1,1)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)