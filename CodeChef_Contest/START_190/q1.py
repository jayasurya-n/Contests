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

        s = ['0']+list(s)+['0']
        used = [False]*(n+1)
        for i in range(1,n+1):
            if(s[i]=='0'):
                if(s[i-1]=='1' and not used[i-1]):
                    used[i-1]=True
                elif(s[i+1]=='1' and not used[i+1]):
                    used[i+1]=True
                else:return no
        return yes

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "Yes","No"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)