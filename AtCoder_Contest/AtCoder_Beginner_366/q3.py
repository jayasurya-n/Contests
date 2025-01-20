from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        q = int(input().strip())
        map = dict()
        
        for i in range(q):    
            arr = input().strip().split()
            if(len(arr)==1):print(len(map))
            else:
                type,x = arr
                if(type=='1'):map[x] = map.get(x,0)+1
                elif(type=='2'):
                    map[x] = map.get(x,0)-1
                    if(map[x]==0):map.pop(x)
                        

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        Solution().run()