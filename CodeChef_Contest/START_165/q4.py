from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log


class Solution:
    def run(self):
        n = int(input().strip())
        s = input().strip()
        
        violations = []
        for i in range(n-1):
            if s[i]==s[i+1]:violations.append(i)
        
        if(len(violations)==0):return True
        elif(len(violations)>2):return False
        
        def can_be_alternating(s,L,R):
            n = len(s)
            L = max(0, L)
            R = min(n, R)
            revs = s[:L] + s[L:R][::-1] + s[R:]
            
            for i in range(n-1):
                if revs[i]==revs[i+1]:return False
            return True

        
        if(len(violations)==1):
            v = violations[0]
            return can_be_alternating(s, v-1, v+1)
        
        if len(violations) == 2:
            v1,v2 = violations
            return can_be_alternating(s, v1+1, v2+1)

if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        if(ans):print(yes)
        else:print(no)