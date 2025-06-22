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
        arr = lii()
        mod = 998244353

        freq = [0]*(n+2)
        for num in arr:freq[num]+=1

        missing,not_misssing = 0,1
        cnt = freq[0]
        ans = -1
        for k in range(1,n+2):
            ways = pow(2,freq[k-1],mod)-1
            
            missing = missing*ways+not_misssing
            missing%=mod

            not_misssing*=ways
            not_misssing%=mod

            cnt+=freq[k]
            ans+=k*missing*pow(2,n-cnt,mod)
            ans%=mod
        return ans


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)