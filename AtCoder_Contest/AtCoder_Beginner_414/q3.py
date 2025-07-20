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
        a = ii()
        n = ii()

        def check(s):
            num = int(s)
            ans = []
            while num>0:
                ans.append(num%a)
                num//=a
            return ans==ans[::-1]

        ans = 0
        q = deque([])
        for digit in range(1,min(10,n+1)):q.append(str(digit))

        while q:
            s = q.popleft()
            if(check(s)):ans+=int(s)

            length = len(s)
            if(length%2==1):
                new = s[:(length//2)+1]+s[length//2]+s[(length//2)+1:]
                if(int(new)<=n):q.append(new)
            else:
                for digit in range(0,10):
                    new = s[:(length//2)]+str(digit)+s[(length//2):]
                    if(int(new)<=n):q.append(new)
        return ans


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)