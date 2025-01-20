from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        x,y,k = list(map(int,input().strip().split()))
        r = k//2
        for i in range(-r,r+1):
            if(k%2==1):
                print(x-i,y)
            else:
                if(i!=0):print(x-i,y)
    
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        Solution().run()