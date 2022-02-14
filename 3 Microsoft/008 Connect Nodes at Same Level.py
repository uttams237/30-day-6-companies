class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        now=[root]
        nextt=[]
        
        while len(now)>0:
            temp=now.pop(0)
            
            if temp.left:
                nextt.append(temp.left)
                
            if temp.right:
                nextt.append(temp.right)
                
            if len(now)==0:
                for i in range(len(nextt)-1):
                    nextt[i].nextRight= nextt[i+1]
                    
                now= nextt
                nextt=[]
