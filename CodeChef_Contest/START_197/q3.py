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
        s = si()

        def check(mid):
            parts = 0
            zeros_score = ones_score = 0
            for i in range(n):
                if(s[i]=='0'):zeros_score+=1
                else:ones_score = 1+max(ones_score,zeros_score)

                if(max(zeros_score,ones_score)>=mid):
                    parts+=1
                    zeros_score = ones_score = 0

            return parts>=k


        low,high = 0,n
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):low = mid+1
            else:high = mid-1
        return high


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)