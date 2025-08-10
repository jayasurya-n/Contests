import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n,k = lii()
        a = lii()
        b = lii()

        arr = []
        ans = 0
        for i in range(n):
            if(a[i]>b[i]):arr.append((b[i],a[i]))
            else:arr.append((a[i],b[i]))
            ans+=abs(a[i]-b[i])
        
        arr.sort(key=lambda x:x[0])

        mini = 10**15
        for i in range(n-1):
            a1,b1 = arr[i]
            a2,b2 = arr[i+1]
            if(a2<=b1):
                mini = 0
                break
            else:mini = min(a2-b1,mini)
        
        return ans+2*mini


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)