from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,x = list(map(int,input().strip().split()))
        return pow(2,n+1)-pow(2,n-x+2)+2





# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())