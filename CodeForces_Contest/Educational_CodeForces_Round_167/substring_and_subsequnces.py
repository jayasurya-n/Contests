class Solution:
    def minimumLength(self,a,b):
        ans = len(a)+len(b)
        common = 0

        for i in range(len(b)):
            j = i
            for k in range(len(a)):
                if(j<len(b) and a[k]==b[j]):j+=1
            common = max(common,j-i)
        return ans-common


t = int(input().strip())
for i in range(t):
    a = input().strip()
    b = input().strip()
    print(Solution().minimumLength(a,b))
