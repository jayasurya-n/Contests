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
        n,m = lii()
        matrix = []
        for _ in range(n):
            matrix.append(lii())
        
        maxi = max([max(row) for row in matrix])
        indices = []

        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==maxi):
                    indices.append((i,j))
        
        ok = False
        r = indices[0][0]
        cols = set()
        for i,j in indices:
            if(i==r):continue
            cols.add(j)
        
        if(len(cols)<=1):ok = True

        c = indices[0][1]
        rows = set()
        for i,j in indices:
            if(j==c):continue
            rows.add(i)
        
        if(len(rows)<=1):ok = True
        
        return maxi-1 if ok else maxi

    
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)