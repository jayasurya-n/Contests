from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        s = input().strip()
        
        def solve(s,temp):
            ans = 0
            for i,ch in enumerate(s):
                if(ch!=temp[i%3]):ans+=1
            return ans

        return min(solve(s,"RGB"),solve(s,"RBG"),
                   solve(s,"GBR"),solve(s,"GRB"),
                   solve(s,"BGR"),solve(s,"BRG"))
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)