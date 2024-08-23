import numpy as np

def definirmatriz(a,b,c,d,e,f,g,h,i,j,k,l):
    
    matrix = np.array([[a,b,c],
                       [d,e,f],
                       [g,h,i]])
    
    b = [j,k,l]
    
    x,y,z = np.linalg.solve(matrix,b)
    
    return x,y,z


print(definirmatriz(2,-3,1,3,1,1,-1,-2,-1,2,-1,1))


