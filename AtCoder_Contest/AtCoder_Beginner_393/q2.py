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
        a = []
        c = []
        hash = set()
        for i in range(len(s)):
            if(s[i]=='A'):a.append(i)
            elif(s[i]=='B'):hash.add(i)
            elif(s[i]=='C'):c.append(i)
        
        ans = 0
        for i in a:
            for k in c:
                if(k>i):
                    ind = (i+k)
                    if (ind&1==0 and ind//2 in hash):ans+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)