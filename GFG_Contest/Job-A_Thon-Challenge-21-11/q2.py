from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def numWays(self, n: int, k: int, m: int) -> int:
        dp = [[[0]*m for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n+1):dp[i][0][0] = 1

        for i in range(1,n+1):
            for j in range(1, min(i+1,k+1)):
                for r in range(m):
                    dp[i][j][r] = (dp[i-1][j][r] + dp[i-1][j-1][(r-(i-1) + m) % m])%(10**9+7)
        return dp[n][k][0]
                    
# time complexity: O(nmk)
# space complexity: O(nmk)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,m,k = list(map(int,input().strip().split()))
        print(Solution().numWays(n,k,m))