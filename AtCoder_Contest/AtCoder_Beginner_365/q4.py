from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        s = input().strip()

        dp = [[0]*3 for _ in range(n+1)]
        
        # ('R',0),('P',1),('S',2)
        
        for i in range(1,n+1):
            if(s[i-1]=='R'):
                dp[i][0] = max(dp[i-1][1],dp[i-1][2])
                dp[i][1] = max(dp[i-1][0],dp[i-1][2])+1
                dp[i][2] = -sys.maxsize
                
            if(s[i-1]=='P'):
                dp[i][0] = -sys.maxsize
                dp[i][1] = max(dp[i-1][0],dp[i-1][2])
                dp[i][2] = max(dp[i-1][0],dp[i-1][1])+1
                
            if(s[i-1]=='S'):
                dp[i][0] = max(dp[i-1][1],dp[i-1][2])+1
                dp[i][1] = -sys.maxsize
                dp[i][2] = max(dp[i-1][0],dp[i-1][1])
        
        return max(dp[n][0],dp[n][1],dp[n][2])

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())