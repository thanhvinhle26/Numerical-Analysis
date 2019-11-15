import numpy as np
def inverse(A):
    n,_=A.shape
    if n==1:
        return 1/A
    elif n>1:
        start=1/A[0,0]
        for i in range(n-1):
            alpha11=start
            alpha12=A[:(i+1),i+1].reshape(i+1,1)
            alpha21=A[i+1,:i+1]
            alpha22=A[i+1,i+1]
            if i==0:
                X=alpha11*alpha12
            else :
                X=alpha11@alpha12
            if i==0:
                Y=alpha21*alpha11
            else :
                Y=alpha21@alpha11
                Y=Y.reshape(1,-1)
            if i==0:
                theta=alpha22-Y*alpha12
            else :
                theta=alpha22-Y@alpha12           
            if i==0:
                beta11=alpha11+(1/theta)*(X*Y)
            else :
                beta11=alpha11+(1/theta)*(X@Y)            
            beta12=-(1/theta)*X
            beta21=-(1/theta)*Y
            beta22=1/theta
            tempt_result=np.vstack((np.hstack((beta11,beta12)),np.hstack((beta21,beta22))))
            start=tempt_result
            np.savetxt('output.txt',tempt_result)    
        return tempt_result