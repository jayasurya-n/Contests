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
        n,q = lii()
        arr = lii()
        arr = [-1]+arr
        
        index = [-1]*(n+1)
        for i in range(1,n+1):
            index[arr[i]] = i
        
        ans = []
        for _ in range(q):
            l,r,k = lii()
            id = index[k]
            if(l>id or id>r):
                ans.append(-1)
                continue
            
            s = b = 0
            ss = bb = 0
            while(l<=r):
                m = (l+r)>>1
                if(arr[m]==k):break
                if(id<m):
                    if(arr[m]<k):b+=1
                    else:bb+=1
                    r = m-1   
                else:
                    if(arr[m]>k):s+=1
                    else:ss+=1
                    l = m+1
            
            if(b+bb>n-k or s+ss>k-1):
                ans.append(-1)
                continue
            
            cnt = 2*min(b,s)
            diff = abs(b-s)
            if(b>s):
                if(diff>n-k-bb):ans.append(-1)
                else:ans.append(cnt+2*diff)
            else:
                if(diff>k-1-ss):ans.append(-1)
                else:ans.append(cnt+2*diff)
                    
        return ans
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)