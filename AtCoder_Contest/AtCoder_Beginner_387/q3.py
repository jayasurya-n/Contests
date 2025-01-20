from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

def nCr(n,r):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

def prefixSum1D(arr,n):
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1,n):prefix[i] = prefix[i-1]+arr[i]
    return prefix

def prefixSum2D(arr,m,n):
    prefix = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            prefix[i][j] = arr[i][j]
            if i>0:prefix[i][j] += prefix[i-1][j]
            if j>0:prefix[a][b] += prefix[i][j-1]
            if i>0 and j>0:prefix[i][j] -= p[i-1][j-1]
    return prefix

class Solution:
    def run(self):
        l,r = list(map(int,input().strip().split()))
        
        count = 0

        # Iterate over possible most significant digits (1–9)
        for msd in range(1, 10):
            queue = [msd]  # Start building numbers with the current MSD
            
            while queue:
                current = queue.pop(0)

                # Count the number if it's in the range [L, R]
                if l<= current <=r:
                    count += 1

                # Generate new numbers by appending smaller digits
                last_digit = current % 10
                for next_digit in range(last_digit - 1, -1, -1):
                    next_number = current * 10 + next_digit
                    if next_number <= r:
                        queue.append(next_number)
        return count

if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)