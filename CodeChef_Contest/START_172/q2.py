from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        a = input().strip()
        b = input().strip()
        
        indices = []
        for i in range(len(b)-1,-1,-1):
            end = indices[-1]-2 if indices else len(a)-1
            found = False
            for j in range(end,-1,-1):
                if(b[i]==a[j]):
                    indices.append(j+1)
                    found = True
                    break
            if(not found):return -1
        
        ans = len(a)*(len(a)+1)//2 - sum(indices)
        ans-= ((len(a)-len(b)-1)*(len(a)-len(b)))//2
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)