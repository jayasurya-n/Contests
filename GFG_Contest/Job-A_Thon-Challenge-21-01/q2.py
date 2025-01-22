from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def xorPair(self, arr):
        n = len(arr)
        hash = defaultdict(int)
        hash[0]=-1
        def solve(ind,xor):
            hash[xor]+=1
            for i in range(ind,n):
                xor^=arr[i]
                solve(i+1,xor)
                xor^=arr[i]
        solve(0,0)
        ans = 0
        mod = 10**9+7
        for val in hash.values():
            ans = (ans+((val*(val-1))//2)%mod)%mod
        return ans

# time complexity: O(2^n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))