from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        s = input().strip()

        i = 0
        c1,c0 = 0,0
        while(i<n):
            if(s[i]=='1'):
                c1+=1
                i+=1
            else:
                while(i<n and s[i]=='0'):
                    i+=1
                c0+=1
        
        return "Yes" if c1>c0 else "No"




# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())