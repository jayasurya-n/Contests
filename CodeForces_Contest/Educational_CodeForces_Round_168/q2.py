from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        grid = []
        grid.append([x for x in input().strip()])
        grid.append([x for x in input().strip()])

        blocked = True
        for i in range(2):
            for j in range(n):
                if(grid[i][j]=='.'):blocked=False
        
        if(blocked):return 0
        
        ans = 0
        for j in range(1,n-1):
            if(grid[0][j]=='.' and grid[1][j]=='.'):
                if(grid[1][j-1]=='x' and grid[1][j+1]=='x' and grid[0][j-1]=='.' and grid[0][j+1]=='.'):ans+=1
                elif(grid[0][j-1]=='x' and grid[0][j+1]=='x' and grid[1][j-1]=='.' and grid[1][j+1]=='.'):ans+=1
        return ans



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())