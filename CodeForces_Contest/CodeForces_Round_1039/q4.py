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
        arr = lii()

        # dp[i] sum of lenght of i starting at i 
        dp = [0]*n
        dp[n-1] = 1

        for i in range(n-2,-1,-1):
            if(arr[i]>arr[i+1]):dp[i] = dp[i+1]+n-i
            else:dp[i] = dp[i+1]+1
        return sum(dp)

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)