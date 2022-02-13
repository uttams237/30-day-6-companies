def spiralPrint(mat, nRows, mCols):
    if nRows==0 or mCols==0 :
        return
    left,right = 0,mCols
    up,down = 0,nRows
    count=0
    ii,jj,total=left,up,(nRows*mCols)
    while True:
        for i in range(left,right):
            print(mat[jj][i] , end=" ")
            ii=i
            count+=1
            if count==total:
                return
        up+=1

        for j in range(up,down):
            print(mat[j][ii] , end=" ")
            jj=j
            count+=1
            if count==total:
                return
        right-=1

        for i in range(right-1,left-1,-1):
            print(mat[jj][i] , end=" ")
            ii=i
            count+=1
            if count==total:
                return
        down-=1

        for j in range(down-1,up-1,-1):
            print(mat[j][ii] , end=" ")
            jj=j
            count+=1
            if count==total:
                return
        left+=1
