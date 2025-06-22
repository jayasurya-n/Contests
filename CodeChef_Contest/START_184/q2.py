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
        
        hash = defaultdict(int)
        for num in arr:hash[num]+=1
        
        for num in range(n//2):
            if(hash[num]+hash[n-1-num])!=2:return 0
        
        if(n%2==1 and hash[n//2]!=1):return 0
        return pow(2,n//2,mod)
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)