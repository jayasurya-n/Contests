from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        
        n,t,a = list(map(int,input().strip().split()))
        diff = n-t-a
        if(min(t,a)+diff<max(t,a)):return "Yes"
        return "No"
    
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())