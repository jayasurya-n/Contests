from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        s = input().strip()
        t = input().strip()
        
        if(s==t):return "Yes"
        if(s[0]=='0' and t[0]=='1'):return "No"
        if(s[0]=='1'):return "Yes"
        one = False
        for i in range(1,len(s)):
            if(s[i]==t[i]):continue
            if(s[i]=='1'):one = True
            if(s[i]=='0' and t[i]=='1' and one==False):return "No"
        return "Yes"
        




# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())