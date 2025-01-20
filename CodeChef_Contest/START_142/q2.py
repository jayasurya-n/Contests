from typing import List,Optional
import sys,math
class Solution:
    def func(self, x) -> Optional[int]:
        temp = x
        nearestTwoPower = 1
        while(nearestTwoPower<x):
            if(nearestTwoPower*2>x):break
            else:nearestTwoPower*=2
        return (x-nearestTwoPower)*2




# time complexity: O(logn)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        x = int(input().strip())
        print(Solution().func(x))