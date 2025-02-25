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
        stack = []
        
        for i in range(len(s)-1,-1,-1):
            if(not stack or s[i]!='W' or stack[-1]!='A'):
                stack.append(s[i])
                continue
            
            if(s[i]=='W' and stack[-1]=='A'):
                stack.pop()
                stack.append('C')
                stack.append('A')
        
        return "".join(stack[::-1])


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)