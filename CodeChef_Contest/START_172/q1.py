from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,x = list(map(int,input().strip().split()))
        nums = list(map(int,input().strip().split()))
        
        def solve(nums):
            ans,cnt = 0,1
            for i in range(n-1):
                if(nums[i]<=nums[i+1]):cnt+=1
                else:cnt = 1
                ans = max(ans,cnt)
            ans = max(ans,cnt)
            return ans

        ans = solve(nums)
        for i in range(n-1):
            if(nums[i]>nums[i+1]):
                temp = nums[i+1]
                nums[i+1]*=x
                ans = max(ans,solve(nums))
                nums[i+1] = temp
        return ans 

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)