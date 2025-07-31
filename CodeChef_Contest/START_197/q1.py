import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        arr = lii()

        odd = even = 0
        for i in range(n):
            if(arr[i]%2==1):odd+=1
            else:even+=1
        
        return yes if odd==1 and even==n-1 else no

if __name__ == "__main__":
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)