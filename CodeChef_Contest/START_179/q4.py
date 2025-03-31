from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        arr.sort()
        q = ii()
        
        def bsIndex(nums,target):
            # works like bisect.left
            # if target is lesser than smallest then index=0
            # if target is larger than largest  then index=n
            low,high = 0,len(nums)-1
            while(low<=high):
                mid = (low+high)>>1
                if(nums[mid]>=target):high = mid-1
                else:low = mid+1
            return low
        
        tsum = sum(arr)
        for _ in range(q):
            x,y = lii()
            ans = 10**18
            ind = bsIndex(arr,x)
            if(ind<n):
                cnt = max(0,y-(tsum-arr[ind]))
                ans = min(ans,cnt)
            if(ind>0):
                cnt = x-arr[ind-1]+max(0,y-(tsum-arr[ind-1]))
                ans = min(ans,cnt)
            print(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()