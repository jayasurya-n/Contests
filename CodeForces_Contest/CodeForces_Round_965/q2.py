from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        n = int(input().strip())
        p = list(map(int,input().strip().split()))
            
        for i in range(n):
            if(p[i]!=n):print(p[i]+1,end=" ")
            else:print(1,end=" ")
        print()
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        Solution().run()