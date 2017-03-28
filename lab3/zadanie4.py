import numpy as np 
import numpy.linalg 


A=np.array([[-1,1,1,0,0], [1,0,0,1,0], [0,1,0,0,1]]); 
B=np.array([1,3,2]); 
print A 
print B
max=0

C =np.array([[0,0,0],[0,0,0],[0,0,0]])


for p in range (0,5-3+1):
    for q in range (p+1,5-3+2):
        for r in range (q+1,5-3+3):
            kolumny = [p, q, r]
            for i in range (0,3):
                for j in range (0,3):
                    C[i][j]= A[j][kolumny[i]]
            if np.linalg.det(C) !=0:
                Ce=np.linalg.inv(transpose(C))
                D=np.linalg.solve(transpose(C),transpose(B))
                pom=D[0]+D[1]
                if max<pom:
                    max=pom
print max
