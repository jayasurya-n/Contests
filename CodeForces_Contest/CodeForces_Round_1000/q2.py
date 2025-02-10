from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,l,r = list(map(int,input().strip().split()))
        nums = list(map(int,input().strip().split()))
        
        l-=1
        r-=1
        target = sorted(nums[l:r+1])
        first = sorted(nums[:l])
        second = sorted(nums[r+1:])

        def getMinsum(target,arr):
            tsum = sum(target)
            if(not arr):return tsum
            ans = curr = tsum
            
            for i in range(min(len(arr),len(target))):
                curr+=arr[i]-target[len(target)-1-i]
                ans = min(ans,curr)
            return ans
        
        return min(getMinsum(target,first),getMinsum(target,second))
            
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)