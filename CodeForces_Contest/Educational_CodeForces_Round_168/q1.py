from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        s = input().strip()
        ch = ''
        for i in range(26):
            if(chr(i+97) not in s):
                ch = chr(i+97)
                break
        
        ans = ""
        bool = False
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                bool = True
                if(ch==''):
                    if(s[i]=='a'):ch = 'b'
                    elif(s[i]=='z'):ch = 'y'
                    else:ch = chr(ord(s[i])+1)
                ans = s[:i]+ch+s[i:]
                return ans

        if(bool==False):
            if(ch==''):
                if(s[i]=='a'):ch = 'b'
                elif(s[i]=='z'):ch = 'y'
                else:ch = chr(ord(s[i])+1)
            return s+ch
        

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())