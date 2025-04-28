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
        x,k = lii()
        if(k>=2 and x!=1):return no
        res = None
        if(k==1):res = x
        else:res = int('1'*k)
        
        def check_prime(n):
            if(n==1):return no 
            for i in range(2,int(n**0.5)+1):
                if(n%i==0):return no
            return yes
        
        return check_prime(res)
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)