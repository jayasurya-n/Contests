from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        
        def bsIndex(nums,target):
            low,high = 0,len(nums)-1
            while(low<=high):
                mid = (low+high)//2
                if(nums[mid]>=target):high = mid-1
                else:low = mid+1
            return low
        
        b.sort()
        for i in range(m):a[0] = min(a[0],b[i]-a[0])
            
        for i in range(1,n):
            mini,maxi = a[i],a[i]
            ind = bsIndex(b,a[i-1]+a[i])
            if(ind<len(b)):
                mini = min(mini,b[ind]-a[i])
                maxi = max(maxi,b[ind]-a[i])
                
            if(mini>=a[i-1]):a[i] = mini
            elif(maxi>=a[i-1]):a[i] = maxi
            else:return no
        return yes

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)