import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        l,r = lii()

        def solve(r):
            if(r<=1):return 0
            
            arr = [2,3,5,7]
            ans = 0
            for num in range(1,1<<4):
                val = 1
                cnt = 0
                for i in range(4):
                    if((num>>i)&1==1):
                        val*=arr[i]
                        cnt+=1

                # print("val,cnt,r//val",val,cnt,r//val)
                if(cnt%2==1):ans+=r//val
                else:ans-=r//val
            
            return (r-1)-ans

        return solve(r)-solve(l-1)

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)