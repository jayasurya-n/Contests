class Solution:
    def breakString(self,s):
        # cnt = 0
        # for i in range(-1,len(s)):
        #     if(s[:i+1]==s[i+1:2*i+2]):
        #         for j in range(2*i+2,len(s)+1):
        #             if(s[2*i+2:j+1]==s[j+1:]):
        #                 cnt+=1
        #                 # print(s[:i+1],s[i+1:j+1],s[j+1:])        
        # return cnt
        n = len(s)
        if n < 3:
            return 0
        
        prefix = [0] * n
        suffix = [0] * n
        
        for i in range(1, n):
            if s[:i] == s[i:2*i] and 2 * i <= n:
                prefix[i - 1] += 1
        
        for i in range(n - 1, 0, -1):
            if s[i:] == s[i - (n - i):i] and i - (n - i) >= 0:
                suffix[i] += 1
        
        cnt = 0
        for i in range(1, n):
            if prefix[i - 1] and suffix[i]:
                cnt += 1
        
        return cnt

t = int(input().strip())
for i in range(t):
    s = input().strip()
    print(Solution().breakString(s))
