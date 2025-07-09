from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if(n<=2):return ""

        # min cost to make good strings till i
        dp = [[10**7]*26 for _ in range(n+1)]
        for j in range(26):dp[0][j] = 0

        best = [[""]*26 for _ in range(n+1)]

        for i in range(3,n+1):
            for j in range(26):
                candidate = best[i-1][j]+chr(97+j)
                if(dp[i][j]> dp[i-1][j]+abs(ord(caption[i-1])-(97+j))):
                    dp[i][j] = dp[i-1][j]+abs(ord(caption[i-1])-(97+j))
                    best[i][j] = candidate

            mini = min(dp[i-3])
            ks   = [k for k in range(26) if dp[i-3][k]==mini]
            for j in range(26):
                candidate = min([best[i-3][k]+chr(97+j)*3 for k in ks])
                ope = 0
                for k in range(3):ope+=abs(ord(caption[i-1-k])-(97+j))
                if((dp[i][j]>mini+ope) or 
                    (dp[i][j]==mini+ope and candidate<best[i][j])):
                    dp[i][j] = mini+ope
                    best[i][j] = candidate
        
        mini = min(dp[n])
        return min(best[n][j] for j in range(26) if dp[n][j]==mini)

# time complexity: O(26n)
# space complexity: O(26n^2)
if __name__ == "__main__":
    for _ in range(ii()):
        caption = si()
        print(Solution().minCostGoodCaption(caption))