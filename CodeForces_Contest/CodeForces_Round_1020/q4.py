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
        n,m = lii()
        a = lii()
        b = lii()
        
        p = [10**10]*m
        j = 0
        for i in range(n):
            if(j>=m):break
            if(a[i]>=b[j]):
                p[j] = i
                j+=1
        
        s = [-10**10]*m
        j = m-1
        for i in range(n-1,-1,-1):
            if(j<0):break
            if(a[i]>=b[j]):
                s[j] = i
                j-=1 
        
        if(s[0]>=0):return 0
        if(m==1):return b[0]
        
        ans = 10**10
        if(s[1]!=-10**10):ans = min(ans,b[0])
        if(p[m-2]!=10**10):ans = min(ans,b[m-1])
        
        for j in range(1,m-1):
            if(p[j-1]<s[j+1]):ans = min(ans,b[j])
        
        return ans if ans!=10**10 else -1
            

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)