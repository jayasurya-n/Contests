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
        x = lii()
        pos = [-1]*(n+1)
        
        for i,num in enumerate(x,1):pos[num] = i
        for i in range(1,n+1):
            if(pos[i]==-1):
                f,s = i,1 if i!=1 else 2
                print("?",f,s,flush=True)
                ans1 = ii()
                
                print("?",f,s,flush=True)
                ans2 = ii()
                
                print("!",'A' if ans1==0 else 'B')
                return
        
        f,s = pos[1],pos[n]      
        print("?",f,s,flush=True)
        ans1 = ii()
        
        print("?",s,f,flush=True)
        ans2 = ii()
        
        if(ans1==ans2 and ans1>=n-1):print("!",'B')
        else:print("!",'A')

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()