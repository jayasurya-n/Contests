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
        n,m = lii()
        arr = lii()
        for i in range(m):
            if(arr[i]==n):arr[i]=n-1
        
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
        
        arr.sort()
        suffix = [0]*m
        for i in range(m-1,-1,-1):
            suffix[i] = arr[i]+(suffix[i+1] if i<m-1 else 0)
        
        ans = 0
        for i in range(m):
            ind = bsIndex(arr,n-arr[i])
            j = max(ind,i+1)
            temp=(m-j)*(arr[i]-n+1)+(suffix[j] if j<m else 0)
            ans+=2*temp
        return ans
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)