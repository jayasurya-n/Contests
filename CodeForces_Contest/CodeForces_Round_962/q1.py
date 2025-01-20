from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        return n//4 + (n%4)//2



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())