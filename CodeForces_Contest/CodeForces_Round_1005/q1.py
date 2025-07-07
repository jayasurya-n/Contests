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
        s = si()
        
        ans = 0
        
        i = n-1
        while(i>=0):
            zeros = 0
            while(i>=0 and s[i]=='0'):
                zeros+=1
                i-=1
            
            ones = 0
            while(i>=0 and s[i]=='1'):
                ones+=1
                i-=1
            
            if(ones>0 and zeros>0):ans+=2
            elif(zeros==0):ans+=1
            
        return ans
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)