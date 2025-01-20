from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isPossible(self, n, conditions):
        mask = [0] * n

        for l,r,x in conditions:
            if x == 0:continue
            for i in range(l - 1, r):
                mask[i] |= x

        for i in range(1, n):
            if mask[i] & mask[i - 1] != mask[i - 1]:return False
        return True

# time complexity: O(nk)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))