from typing import List,Optional
import sys
import itertools
class Solution:

    def checkPalindrome(self,s,k):
        n = len(s)
        for i in range(0,n-k+1):
            if(s[i:i+k]==s[i:i+k][::-1]):return True
        return False

    def run(self) -> Optional[list]:
        n,k = list(map(int,input().strip().split()))
        s = input().strip()

        all = set(itertools.permutations(s))
        ans = 0
        for i in all:
            string = "".join(i)
            if(not self.checkPalindrome(string,k)):
                ans+=1
        return ans
        


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())