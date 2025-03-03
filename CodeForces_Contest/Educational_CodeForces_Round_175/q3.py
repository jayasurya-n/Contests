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
        n,k = lii()
        s = si()
        penalty = lii()
        
        def check(x):
            arr = []
            for i in range(n):
                if(s[i]=='B'):
                    if(penalty[i]>x):arr.append(1)
                    else:arr.append(0)
                else:
                    if(penalty[i]>x):arr.append(2)
                    else:arr.append(0)
                    
            ans = 0
            i = 0
            while(i<n):
                if(arr[i]==1):
                    while(i<n and arr[i]!=2):i+=1
                    ans+=1
                i+=1
            return ans<=k
                    
        low,high = 0,max(penalty)
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        return low
                

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)