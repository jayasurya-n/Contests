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

        # if(s=='0'*n or s=='1'*n):return n

        start = i = 0
        while i<n and s[i]==s[0]:
            i+=1
            start+=1

        end,j = 0,n-1
        while j>=0 and s[j]==s[n-1]:
            end+=1
            j-=1

        if(j<i):return n
        if(s[0]=='0' and s[n-1]=='0'):return start+end
        if(s[0]=='1' and s[n-1]=='1'):return start+end
        return start+end+1


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)