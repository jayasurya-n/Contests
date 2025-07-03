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
        x,y,z,c = lii()
        if(x==y):return 0
        ans = 2*c

        x,y = sorted((x,y))
        if(y%x!=0):return ans

        # for d in range(x,y+1,x):
        #     if(y%d==0):
        #         ans = min(ans,abs(d-z)+c)
        # return ans

        i = 1
        while i*i<=y:
            if(y%i==0):
                if(i%x==0):ans = min(ans,abs(i-z)+c)
                if((y//i)%x==0):ans = min(ans,abs((y//i)-z)+c)
            i+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)