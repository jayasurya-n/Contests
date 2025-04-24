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
        s = si()
        t = si()
        
        s = list(s)
        t = list(t)
        
        if(s==t):
            print(0)
            return 
        
        if(s[0]!=t[0]):
            print(-1)
            return
        
        closets_ones = [-1]*n
        curr = -1
        for i in range(n):
            closets_ones[i] = curr
            if s[i]=='1':curr=i
        
        # print(closets_ones)
        
        ans = []
        for i in range(n-1,0,-1):
            if(s[i]==t[i]):continue
            j = closets_ones[i]
            if(j==-1):
                print(-1)
                return 
            
            for k in range(j,i):
                ans.append(k+1)
                s[k+1] = '1' if s[k+1]=='0' else '0'
            
            for k in range(i-2,j-1,-1):
                if(s[k+1]==t[k+1]):continue
                ans.append(k+1)
                s[k+1] = '1' if s[k+1]=='0' else '0'
        
        if(len(ans)>3*n):
            print(-1)
            return
        
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()