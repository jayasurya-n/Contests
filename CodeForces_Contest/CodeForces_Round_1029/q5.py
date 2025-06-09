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
        a = lii()
        b = lii()

        hashA = [[] for _ in range(n+1)]
        hashB = [[] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            if(a[i]==b[i]):return i+1

            # a[i] in A
            for index in hashA[a[i]]:
                if((index-i)%2)==1:return i+1
                elif((index-i)>=2):return i+1

            # b[i] in B
            for index in hashB[b[i]]:
                if((index-i)%2)==1:return i+1
                elif((index-i)>=2):return i+1
            
            # a[i] in B
            for index in hashB[a[i]]:
                if((index-i)%2)==0:return i+1
                elif((index-i)>=2):return i+1

            # b[i] in A
            for index in hashA[b[i]]:
                if((index-i)%2)==0:return i+1
                elif((index-i)>=2):return i+1

            hashA[a[i]].append(i)
            hashB[b[i]].append(i)
        
        return 0


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)