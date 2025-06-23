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

        def solve(s):
            freq = [0]*26
            freq[ord(s[0])-97]+=1
            for i in range(1,n-1):
                if(freq[ord(s[i])-97]!=0):return True
                freq[ord(s[i])-97]+=1
            return False

        if(solve(s) or solve(s[::-1])):return yes
        return no



if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)