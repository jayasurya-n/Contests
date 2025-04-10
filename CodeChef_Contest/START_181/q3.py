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
        m,n = lii()
        matrix = []
        for _ in range(m):matrix.append(lii())

        ans = 0
        for sx in [-1,1]:
            for sy in [-1,1]:
                hash = defaultdict(int)
                for i in range(m):
                    for j in range(n):
                        d = matrix[i][j]-(sx*i+sy*j)
                        hash[d]+=1
                ans = max(ans,max(hash.values()))
        
        return n*m-ans
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)