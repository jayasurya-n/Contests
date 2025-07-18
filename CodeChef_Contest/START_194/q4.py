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
        n = int(input())
        matrix = [list(map(int,input().strip())) for _ in range(n)]
        mod = 10**9+7

        ans = 1
        for i in range(n):
            ans*=matrix[i].count(1)
            ans%=mod

        palindromes = 1
        for i in range(n//2):
            cnt = 0
            for j in range(n):
                if(matrix[i][j]==1 and matrix[i+(n//2)][j]==1):
                    cnt+=1
            palindromes*=cnt
            palindromes%=mod

        return (ans-palindromes+mod)%mod


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)