from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))

        dp = [[0]*n for _ in range(n)]

        # for i in range(1,n):
        #     for 




# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())