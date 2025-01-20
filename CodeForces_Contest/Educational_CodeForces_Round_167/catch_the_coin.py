class Solution:
    def canReach(self,x,y):
        if(y>=-1):return "YES"
        else:return "NO"

t = int(input().strip())
for i in range(t):
    x,y = list(map(int,input().strip().split()))
    print(Solution().canReach(x,y))
