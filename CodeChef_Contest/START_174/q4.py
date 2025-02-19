from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        
        mex = 0
        hash = set()
        for num in arr:hash.add(num)
        while(mex<n and mex in hash):mex+=1
        
        total = sum(arr)
        if(mex==0):
            mini = sys.maxsize
            for i in range(1,n-1):
                mini = min(mini,arr[i])
            ans = [2*arr[0]+2*arr[n-1]-total,total-2*mini]
            return ans
        
        left = -1
        prefix = set([])
        for i in range(n):
            if(arr[i]<mex):prefix.add(arr[i])
            if(len(prefix)==mex):
                left = i
                break
        
        
        right = -1
        suffix = set([])
        for i in range(n-1,-1,-1):
            if(arr[i]<mex):suffix.add(arr[i])
            if(len(suffix)==mex):
                right = i
                break
        
        middle = set()
        for i in range(left+1,right):
            if(arr[i]<mex):middle.add(arr[i])
        
        if(left==-1 or right==-1 or 
           left+1>right-1 or len(middle)!=mex):return [-1,-1]
        
        min_sum = 2*sum(arr[:left+1]) + 2*sum(arr[right:]) - total
        
        i = j = left+1
        w_sum = 0
        middle = defaultdict(int)
        middle_sum = 10**18
        
        while(j<right):
            w_sum+=arr[j]
            if(arr[j]<mex):middle[arr[j]]+=1
            
            while(i<j and len(middle)==mex):
                if(arr[i]<mex):
                    if(middle[arr[i]]==1):break
                    middle[arr[i]]-=1
                w_sum-=arr[i]
                i+=1
            
            if(len(middle)==mex):
                middle_sum = min(middle_sum,w_sum)
            j+=1

        max_sum = total-2*middle_sum
        return [min_sum,max_sum]
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)