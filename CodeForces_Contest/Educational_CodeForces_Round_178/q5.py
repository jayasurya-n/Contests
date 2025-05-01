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
        n,k = lii()
        s = si()
        
        next = [[n]*k for _ in range(n+1)]
        for j in range(k):
            prev = n
            for i in range(n-1,-1,-1):
                if(s[i]==chr(97+j)):prev = i
                next[i][j] = prev
        
        dp = [n+1]*(n+1)
        dp[n] = 0
        dp[n-1] = 1
        # dp[i]: minimum steps to go from i to n
        # transition: dp[i] = 1+max(dp[next[i+1][c]])
        # base: dp[n] = 0
        
        for i in range(n-2,-1,-1):
            for j in range(k):
                dp[i] = min(dp[i],1+dp[next[i+1][j]])
        
        q = ii()
        for _ in range(q):
            t = si()
            curr = -1
            for i in range(len(t)):
                curr = next[curr+1][ord(t[i])-97]
                if(curr==n):break
            print(dp[curr])
            

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()