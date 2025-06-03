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

        a = [0]*n
        c = [0]*n

        acnt = 0
        for i in range(n):
            if(s[i]=='A'):acnt+=1
            elif(s[i]=='B'):a[i] = acnt
            else:acnt = 0
   
        ccnt = 0
        for i in range(n-1,-1,-1):
            if(s[i]=='C'):ccnt+=1
            elif(s[i]=='B'):c[i] = ccnt
            else:ccnt = 0
        
        ans = 0
        for i in range(n):
            if(s[i]!='B'):continue
            ans+=max(a[i],c[i])
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)