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
        n,x = lii()
        sb = bin(x).count('1')

        if(sb>=n):return x
        rem = n-sb
        if(rem%2==0):return x+n-sb
        else:
            if(x>1):return x+n-sb+1
            elif(x==1):return x+n-sb+3
            elif(x==0):
                if(n==1):return -1
                else:return n+3

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)