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
        s = si()
        n = len(s)
        
        i=0     
        while(i<n//2 and s[i]==s[n-i-1]):i+=1
        if(i>n//2):return 0
        
        s = s[i:n-i]
        # print(s)
        
        def check(s,mid):
            n = len(s)
            hash = defaultdict(int)
            for i in range(mid):hash[s[i]]+=1
            
            for i in range(min(mid,n-mid)):
                ch = s[n-1-i]
                if(ch in hash):
                    hash[ch]-=1
                    if(hash[ch]==0):hash.pop(ch)
                else:return False
            
            for i in range(mid,n//2):
                if(s[i]!=s[n-1-i]):return False
            return True
            
        low,high = 0,len(s)
        while(low<=high):
            mid = (low+high)>>1
            # print("low,mid,high",low,mid,high)
            if(check(s,mid) or check(s[::-1],mid)):high = mid-1
            else:low = mid+1
        return low


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)