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
        n,q = lii()
        matrix = [list(si()),list(si())] #2xn

        def solve(arr):
            cnt = arr.count('1')
            ones = [i for i in range(n) if arr[i]=='1']
            cost = [-1]*n
            for i in range(cnt):
                cost[i] = (cost[i-1] if i>0 else 0)+(ones[i]-i)
            return cost

        prefix_cost = solve(matrix[0])
        suffix_cost = solve(matrix[1][::-1])

        ans = 10**15
        for i in range(n):
            if(prefix_cost[i]==-1 or suffix_cost[n-1-i]==-1):continue
            ans = min(ans,prefix_cost[i]+suffix_cost[n-1-i])
        return ans if ans!=10**15 else -1

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)