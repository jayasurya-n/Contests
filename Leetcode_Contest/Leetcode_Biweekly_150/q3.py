from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect
from sortedcontainers import SortedKeyList

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def upper_greater(mid):
            upper = lower = 0
            for _,y,l in squares:
                if(y>=mid):upper+=l*l
                elif(y+l<=mid):lower+=l*l
                else:
                    upper+=(y+l-mid)*l
                    lower+=(mid-y)*l
            return upper>lower
        
        low,high = 0,2*10**9+1
        precision = 10**(-6)
        while(low<=high):
            mid = (low+high)/2
            if(not upper_greater(mid)):high = mid-precision
            else:low = mid+precision
        return low

# time complexity: O(nlogm)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        squares = []
        for _ in range(n):squares.append(lii())
        print(Solution().separateSquares(squares))