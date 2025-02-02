from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log


class Solution:
    def run(self):
        s = input().strip()
        map = {'N':'S','S':'N','E':'W','W':'E'}
        ans = []
        for ch in s:
            ans.append(map[ch])
        return "".join(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)