import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n,c = lii()
        weights = lii()

        ans = 0
        weights.sort(reverse=True)
        double = 0
        for i in range(n):
            if((weights[i]*(1<<double))>c):
                ans+=1
                continue
            else:
                double+=1
        return ans


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)