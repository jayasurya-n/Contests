from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,x = list(map(int,input().strip().split()))
        ans = 0
        for a in range(1,x-1):
            for b in range(1,x-a):
                c = min(x-a-b, (n-a*b)//(a+b))
                if(c>=1):ans+=c
                else:break
        return ans


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())
