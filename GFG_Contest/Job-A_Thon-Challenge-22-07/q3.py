from typing import List,Optional
from collections import deque, defaultdict
from sortedcontainers import SortedSet
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class SegmentTree:
    def __init__(arr,n):
        self.seg = [0]*4*n
        self.lazy = [0]*4*n
        self.build(0,0,n-1,0,arr)
    
    def build(self,node,low,high,arr):
        if(low==high):
            self.seg[node] = arr[low]
            return
        
        mid = (low+high)>>1
        self.build(2*node+1,low,mid,arr)
        self.build(2*node+2,mid+1,high,arr)
        self.seg[node] = self.seg[2*node+1]+self.seg[2*node+2]   
            
    def rangeQuery(self,node,low,high,l,r):
        if(self.lazy[node]!=0):
            self.seg[node]+=(high-low+1)*self.lazy[node]
            if(low!=high):
                self.lazy[2*node+1]+=self.lazy[node] 
                self.lazy[2*node+2]+=self.lazy[node] 
            self.lazy[node]=0
        
        if(high<l or low>r):return 0
        if(l<=low and high<=r):return self.seg[node]
        
        mid = (low+high)>>1
        left = self.query(2*node+1,low,mid,l,r)
        right = self.query(2*node+2,mid+1,high,l,r)
        return left+right
    
    def rangeUpdate(self,node,low,high,l,r,val):
        if(self.lazy[node]!=0):
            self.seg[node]+=(high-low+1)*self.lazy[node]
            if(low!=high):
                self.lazy[2*node+1]+=self.lazy[node] 
                self.lazy[2*node+2]+=self.lazy[node] 
            self.lazy[node]=0
        
        if(low>r or high<l):return
        if(l<=low and high<=r):
            self.seg[node]+=(high-low+1)*val
            if(low!=high):
                self.lazy[2*node+1]+=val
                self.lazy[2*node+2]+=val 
            return
        
        mid = (low+high)>>1
        self.rangeUpdate(2*node+1,low,mid,l,r,val)
        self.rangeUpdate(2*node+2,mid+1,high,l,r,val)
        self.seg[node] = self.seg[2*node+1]+self.seg[2*node+2]

    # def update(self,node,low,high,pos,value):
    #     if(low==high):
    #         self.seg[node]+=value
    #         return
        
    #     mid = (low+high)>>1
    #     if(pos<=mid):self.update(2*node+1,low,mid,pos,value)
    #     else:self.update(2*node+2,mid+1,high,pos,value)
    #     self.seg[node] = self.seg[2*node+1]+self.seg[2*node+2]

class Solution:
    def RangeSumDigits(self, n : int, arr : List[int], q : int, queries : List[List[int]]) -> List[int]:
        st = SegmentTree(arr)        
        def countDigits(n):
            cnt = 0
            while(n>0):
                cnt+=1
                n//=10
            return cnt
        
        ans = []
        s = SortedSet([i for i in range(n) if arr[i] != 1])
                    
        for query in queries:
            type,l,r = query[0],query[1]-1,query[2]-1
            if(type==2):ans.append(st.rangeQuery(0,0,n-1,l,r))
            else:
                if not s:continue
                temp = []
                pos = bisect.bisect_left(s,l)
                for i in range(pos,len(s)):
                    if(s[i]<l):continue
                    if(s[i]>r):break

                    val = countDigits(arr[s[i]])
                    arr[s[i]] = val
                    st.rangeUpdate(0,0,n-1,s[i],s[i],val)
                    if(val==1):temp.append(s[i])
                
                for index in temp:s.remove(index)
        
        return ans

# time complexity: O((n+q)logn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))