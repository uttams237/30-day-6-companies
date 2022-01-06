class Solution:
    
    
    def doOverlap(self, l1, r1, l2, r2):
        #code here
        
        # def area(l,r):
        #     h= l[1]-r[1]
        #     b= l[0]-r[0]
            
        #     return abs(h*b)
        
        # if area(l1,r1)==0:
        #     return 0
        # if area(l2,r2)==0:
        #     return 0
        
        # for 1 in left
        if r1[0]<l2[0] or r2[0]<l1[0]:
            return 0
            
        # for i to be above
        if r2[1]>l1[1] or r1[1]>l2[1]:
            return 0
            
        return 1
