from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        if(n%4!=0):return 365
        else:
            if(n%100!=0):return 366
            else:
                if(n%400!=0):return 365
                else:return 366
            
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())