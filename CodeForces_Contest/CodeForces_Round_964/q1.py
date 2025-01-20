from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        return sum(int(x) for x in str(n))


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())