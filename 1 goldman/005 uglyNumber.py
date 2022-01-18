class Solution:
	def getNthUglyNo(self,n):
	    arr=[1 for i in range(n)]
	    i2,i3,i5=0,0,0
	    nxt2,nxt3,nxt5=2,3,5
	    
	    for i in range(1,n):
	        ans= min(nxt2,nxt3,nxt5)
	        arr[i]=ans
	        
	        if ans==nxt2:
	            i2+=1
	            nxt2= arr[i2]*2
            if ans==nxt3:
                i3+=1
                nxt3= arr[i3]*3
            if ans==nxt5:
                i5+=1
                nxt5= arr[i5]*5
                
        return arr[-1]
