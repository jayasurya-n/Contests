from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        a1,a2,a4,a5 = list(map(int,input().strip().split()))
        def solve(a3):
            cnt = 0
            if(a1+a2==a3):cnt+=1
            if(a2+a3==a4):cnt+=1
            if(a3+a4==a5):cnt+=1
            return cnt
        return max(solve(a1+a2),solve(a4-a2),solve(a5-a4))

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
        print(ans)