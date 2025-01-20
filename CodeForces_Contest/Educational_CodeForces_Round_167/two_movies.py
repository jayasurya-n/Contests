class Solution:
    def maximumRating(self,a,b,n):
        ans = 0
        a_rating,b_rating = 0,0
        pos,neg = 0,0
        
        for i in range(n):
            if(a[i]>b[i]):a_rating+=a[i]
            elif(a[i]<b[i]):b_rating+=b[i]
            elif(a[i]==1):pos+=1
            elif(a[i]==-1):neg+=1
        
        while(pos):
            if(a_rating>b_rating):b_rating+=1
            else:a_rating+=1
            pos-=1

        while(neg):
            if(a_rating>b_rating):a_rating-=1
            else:b_rating-=1
            neg-=1
        
        return min(a_rating,b_rating)

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    a = list(map(int,input().strip().split()))
    b = list(map(int,input().strip().split()))
    print(Solution().maximumRating(a,b,n))
