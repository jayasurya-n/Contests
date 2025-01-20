from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,k = list(map(int,input().strip().split()))
        grid = [[x for x in input().strip()] for _ in range(n)]

        l = n//k
        ans = [[-1]*l for _ in range(l)]

        for i in range(l):
            for j in range(l):
                ans[i][j] = grid[i*k][j*k]
        return ans



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        ans = Solution().run()
        for row in ans:
            print("".join(row))