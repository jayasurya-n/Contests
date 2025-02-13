from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()

        def seven(n):
            temp = n
            while temp>0:
                digit = temp%10
                if(digit==7):return True
                temp//=10
            return False
        
        def count(n):
            temp = n
            cnt = 0
            while temp>0:
                digit = temp%10
                cnt+=1
                temp//=10
            return cnt

        if(seven(n)):return 0
        
        ans = 11
        length = count(n)
        for l in range(1,length+1):
            adder = int('9'*l)
            for i in range(1,11):
                temp  = n+adder*i
                if(seven(temp)):ans = min(ans,i)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)