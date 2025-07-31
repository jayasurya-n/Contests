import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        A = lii()
        B = lii()

        def check(s):
            tsum = curr = 0.0
            for i in range(n-1,-1,-1):
                curr = min(curr+A[i],(s/(n+1))+B[i])
                tsum+=curr
            return [tsum,curr]

        low,high = 0.0,10**18
        for _ in range(100):
            mid = (low+high)*0.5
            if(check(mid)[0]>=mid):low = mid
            else:high = mid
        return check((low+high)*0.5)[1]


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)