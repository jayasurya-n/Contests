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
        s  = si()
        
        cnt = 0
        prev = '0'
        for ch in s:
            if(ch==prev):cnt+=1
            else:cnt+=2
            prev = ch
        
        ans = cnt
        start = 1 if s[0] == '1' else 0
        
        zero_ones = one_zeros = 0
        for i in range(1,n):
            if(s[i-1]=='0' and s[i]=='1'):zero_ones+=1
            elif(s[i-1]=='1' and s[i]=='0'):one_zeros+=1

        if start+zero_ones>= 2 or one_zeros>=2:ans-=2
        elif (s[-1] == '0' and (start + zero_ones)>=1) or (s[-1] == '1' and one_zeros>=1):ans-=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)