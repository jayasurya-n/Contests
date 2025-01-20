from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        a1,a2,b1,b2 = list(map(int,input().strip().split()))
        def count(a1,a2,b1,b2):
            awins,bwins = 0,0 
            if(a1>b1):awins+=1
            elif(a1<b1):bwins+=1
            
            if(a2>b2):awins+=1
            elif(a2<b2):bwins+=1
            
            if(awins>bwins):return 1
            else:return 0
        
        ans = 0
        ans+=count(a1,a2,b1,b2)
        ans+=count(a1,a2,b2,b1)
        ans+=count(a2,a1,b1,b2)
        ans+=count(a2,a1,b2,b1)
        return ans
        
    
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())