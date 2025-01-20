from typing import List,Optional
from collections import deque
import sys,math
class Solution:
    def run(self):
        n,D = list(map(int,input().strip().split()))
        x,y = [],[]
        for _ in range(n):
            x1,y1 = list(map(int,input().strip().split()))
            x.append(x1)
            y.append(y1)
        
        x.sort()
        y.sort()
    
        x_m = x[n//2]
        y_m = y[n//2]
        
        minD = sum(abs(x_m - x1) + abs(y_m - y1) for x1, y1 in zip(x,y))
        if minD > D:return 0
        rem = D-minD
        
        ans = 0
        for dx in range(-rem, rem+1):
            for dy in range(-(rem-abs(dx)), rem-abs(dx)+1):
                ans += 1
        return ans


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())