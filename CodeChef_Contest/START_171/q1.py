from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        target = "ADVITIYA"
        s = input().strip()
        ans = 0
        for i,ch in enumerate(s):
            ans+=(ord(target[i])-ord(ch)+26)%26
        return ans
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)