from typing import List
import math
import sys
class Solution:
    def countPairs(self,n,k,h):
        ans = 0
        for a in range(1,n+1):
            if a>=h:ans+=n
            else:
                b_max = math.floor(a - ((h-a)/(k-1)))
                if(1<=b_max<=n):ans+=b_max
        return ans            

            
# time complexity:O(n) 
# space complexity:O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n,k,h = list(map(int,input().strip().split()))
        print(Solution().countPairs(n,k,h))