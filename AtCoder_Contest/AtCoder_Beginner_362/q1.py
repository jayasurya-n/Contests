from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        
        r,g,b = list(map(int,input().strip().split()))
        c = input().strip()
        
        arr = [['Red',r],['Green',g],['Blue',b]]
        arr.sort(key=lambda x:x[1])

        if(arr[0][0]!=c):return arr[0][1]
        return arr[1][1]





# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())