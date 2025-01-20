from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        x,y,z = list(map(int,input().strip().split()))
        temp=x
        while(x*y>z):
            x-=1
        return temp-x





# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())