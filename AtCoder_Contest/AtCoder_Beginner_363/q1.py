from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        r = int(input().strip())
        if(r<100):return 100-r
        elif(r<200):return 200-r
        else:return 300-r





# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())