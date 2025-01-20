from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,k = list(map(int,input().strip().split()))
        if(k==0):return 0
        ans = 0
        k-=n
        ans+=1
        if(k<=0):return ans
        for chips in range(n-1,0,-1):
            for cnt in range(2):
                k-=chips
                ans+=1
                if(k<=0):return ans



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())