class Solution:
    def countWays(self,m):
        cnt=0
        # (1*y) + (2*x) = m
        for y in range(m+1):
            x= (m-y)/2
            if x%1==0:
                cnt+=1
                
        return cnt
