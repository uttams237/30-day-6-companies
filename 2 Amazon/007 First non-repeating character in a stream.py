class Solution:
	def FirstNonRepeating(self, A):
	    dq=[]
	    sett=set()
	    ans=""
	    
	    for alp in A:
	        if alp in sett:
	            if alp in dq:
	                dq.remove(alp)
            else:
                dq.append(alp)
                sett.add(alp)
                
            if len(dq)>0:
                ans+=dq[0]
            else:
                ans+="#"
		# Code here
		return ans
