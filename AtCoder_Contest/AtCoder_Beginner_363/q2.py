from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,t,p = list(map(int,input().strip().split()))
        hairs = list(map(int,input().strip().split()))
        cnt = 0
        for i in range(len(hairs)):
            if(hairs[i]>=t):cnt+=1
        if(cnt>=p):return 0
        hairs.sort()
        return t-hairs[n-p]


        

# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())