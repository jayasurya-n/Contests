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
        prefix = lii()
        suffix = lii()

        if(prefix[n-1]!=suffix[0]):return no

        def check(arr):
            ok = True
            for i in range(1,n):
                if(arr[i]>arr[i-1] or arr[i-1]%arr[i]!=0):
                    ok = False
                    break
            return ok

        ok = check(prefix) and check(suffix[::-1])

        suffix = suffix[::-1]
        gcd_arr = prefix[n-1]
        for i in range(n-1):
            if(math.gcd(prefix[i],suffix[n-2-i])!=gcd_arr):
                ok = False
                break
        
        return yes if ok else no
                

if __name__ == "__main__":
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)