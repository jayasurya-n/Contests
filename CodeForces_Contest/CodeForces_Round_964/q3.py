from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n,s,m = list(map(int,input().strip().split()))
        times = [tuple(map(int,input().strip().split())) for _ in range(n)]
        
        times.sort(key = lambda x:x[0])
        
        if(times[0][0]>=s or
           m-times[-1][1]>=s):return "YES"
        
        for i in range(1,n):
            if(times[i][0]-times[i-1][1]>=s):return "YES"
        return "NO"
            
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())