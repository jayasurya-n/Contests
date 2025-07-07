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
        a,b,x,y = lii()
        if(a==b):return 0
        if((a%2==1 and a-1>b) or 
           (a%2==0 and a>b)):return -1

        if(a%2==1 and a-1==b):return y

        diff = b-a
        if(a%2==0):
            xor = (diff+1)//2
            add = diff-xor
            return x*add+min(x,y)*(xor)

        else:
            add = (diff+1)//2
            xor = diff-add
            return x*add+min(x,y)*(xor)



if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)