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
        taste = lii()
        sugar = lii()

        ans = -10**10
        for L in range(0,101):
            tsum = 0
            for i in range(n):
                if(taste[i]>=0 and sugar[i]<=L):
                    tsum+=taste[i]
            ans = max(ans,tsum-L)
        return ans

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)