from typing import List,Optional
import sys
class Solution:
    def func(self, x,y) -> Optional[int]:
       if(y in range(x,x+3) or (x in range(y,y+2))):return "YES"
       else:return "NO"




# time complexity: O(1)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        x,y = list(map(int,input().strip().split()))
        print(Solution().func(x,y))