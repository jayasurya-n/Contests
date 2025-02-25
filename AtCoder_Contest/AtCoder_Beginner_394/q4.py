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
        
        for ch in s:
            if(stack and
               ((stack[-1]=='(' and ch==')') or
               (stack[-1]=='[' and ch==']') or
               (stack[-1]=='<' and ch=='>'))):stack.pop()
            else:stack.append(ch)
        
        return yes if not stack else no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "Yes","No"
    for _ in range(1):
        ans = Solution().run()
        print(ans)