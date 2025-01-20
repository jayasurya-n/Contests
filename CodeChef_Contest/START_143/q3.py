from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        i = n
        ans = []
        val = 1
        while(i>=1):
            if(i>n//2):ans.append(val)
            else:
                val+=1
                ans.append(val)
                n//=2
            i-=1
        return ans[-1],ans[::-1]



        
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        C,arr = Solution().run()
        # print(C)
        for i in arr:
            print(i,end=" ")
        print()