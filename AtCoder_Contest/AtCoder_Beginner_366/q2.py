from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        n = int(input().strip())
        arr = [input().strip() for _ in range(n)]
        m = 0
        for i in arr:m = max(m,len(i))
        
        ans = []
        for j in range(m):
            s = ""
            for i in range(n-1,-1,-1):
                if(j<len(arr[i])):s+=arr[i][j]
                else:s+='*'
            s = s.rstrip('*')
            ans.append(s)        
        for i in ans:
            print(i)

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        Solution().run()