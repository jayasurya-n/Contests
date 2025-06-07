from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        maxi = 0
        nums = []
        for i in range(n-1):
            if(arr[i]==arr[i+1]):continue
            nums.append(arr[i])
        nums.append(arr[-1])
        
        ans = 0
        if(len(nums)==1):return 1
        if(nums[0]>nums[1]):ans+=1
        if(nums[-1]>nums[-2]):ans+=1

        for i in range(1,len(nums)-1):
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):ans+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)