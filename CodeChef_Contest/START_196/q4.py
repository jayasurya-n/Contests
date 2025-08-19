import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class SegmentTree:
    def __init__(self,A,B,k):
        self.n = len(A)
        self.size = 1 <<(self.n-1).bit_length()

        # end0,sum0,end1,sum1
        self.sege0 = [0 for _ in range(2*self.size)] #1-based index
        self.segs0 = [0 for _ in range(2*self.size)] #1-based index
        self.sege1 = [0 for _ in range(2*self.size)] #1-based index
        self.segs1 = [0 for _ in range(2*self.size)] #1-based index
        
        for i in range(self.n):
            a,b = A[i],B[i]
            # start = 0
            if(a+k<b):end0,sum0 = 1,b
            else:end0,sum0 = 0,a
            
            # start = 1
            if(b+k<a):end1,sum1 = 0,a
            else:end1,sum1 = 1,b

            self.sege0[i+self.size] = end0
            self.segs0[i+self.size] = sum0
            self.sege1[i+self.size] = end1
            self.segs1[i+self.size] = sum1
        
        for i in range(self.size-1,0,-1):
            self.sege0[i],self.segs0[i],self.sege1[i],self.segs1[i] = self._merge((self.sege0[2*i],self.segs0[2*i],self.sege1[2*i],self.segs1[2*i]),
                                      (self.sege0[2*i+1],self.segs0[2*i+1],self.sege1[2*i+1],self.segs1[2*i+1]))
    
    def _merge(self,left,right):
        lend0,lsum0,lend1,lsum1 = left
        rend0,rsum0,rend1,rsum1 = right

        # start = 0
        pend0 = rend0 if lend0==0 else rend1
        psum0 = lsum0 + (rsum0 if lend0==0 else rsum1)

        # start = 1
        pend1 = rend0 if lend1==0 else rend1
        psum1 = lsum1 + (rsum0 if lend1==0 else rsum1)

        return (pend0,psum0,pend1,psum1)

    
    def update(self,ind,a,b,k):
        ind+=self.size
        # start = 0
        if(a+k<b):end0,sum0 = 1,b
        else:end0,sum0 = 0,a
        
        # start = 1
        if(b+k<a):end1,sum1 = 0,a
        else:end1,sum1 = 1,b

        self.sege0[ind] = end0
        self.segs0[ind] = sum0
        self.sege1[ind] = end1
        self.segs1[ind] = sum1
        ind//=2
        while ind>=1:
            self.sege0[ind],self.segs0[ind],self.sege1[ind],self.segs1[ind] = self._merge((self.sege0[2*ind],self.segs0[2*ind],self.sege1[2*ind],self.segs1[2*ind]),
                            (self.sege0[2*ind+1],self.segs0[2*ind+1],self.sege1[2*ind+1],self.segs1[2*ind+1]))
            ind//=2

class Solution:
    def run(self):
        n,k = lii()
        A = lii()
        B = lii()

        st = SegmentTree(A,B,k)
        for _ in range(ii()):
            t,i,x = lii()
            i-=1
            if(t==1):A[i] = x
            else:B[i] = x
            st.update(i,A[i],B[i],k)
            print(st.segs0[1]) 

if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()