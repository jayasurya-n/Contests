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

        type1 = type2 = type3 = 0
        for num in arr:
            if(num%3==0):type1+=1
            if(num%3==1):type2+=1
            if(num%3==2):type3+=1
        
        if((type1>=1) or (type2>=3) or (type3>=3) or
           (type2>=1 and type3>=1)):return yes 
        return no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)