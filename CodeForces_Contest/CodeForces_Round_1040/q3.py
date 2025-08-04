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
        arr = []

        for i in range(1,n+1):
            a,b = lii()
            arr.append((a,b,i))
        
        arr.sort(key=lambda x:(x[0],-x[1]))
        ans = []

        last = -1
        for a,b,i in arr:
            if(b>last):
                ans.append(i)
                last = b
        
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()