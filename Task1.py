# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:17:16 2016

@author: HomeUser
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:18:46 2016

@author: HomeUser
"""

import numpy as np
#Your optional code here
#You can import some modules or create additional functions

#LU-Decomposition start

def LUdecomp(A):

    n = len(A)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i,k] != 0.0:
                lam = A[i,k] / A[k,k]
                A[i, k+1:n] = A[i, k+1:n] - lam * A[k, k+1:n]
                A[i, k] = lam
    return A

def LUsolve(A,b):
    n = len(A)
    for k in range(1,n):
        b[k] = b[k] - np.dot(A[k,0:k], b[0:k])
    b[n-1]=b[n-1]/A[n-1, n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(A[k,k+1:n], b[k+1:n]))/A[k,k]
    return b
    
#END OF LU-Decomposition

def lu(A, b):
    # Edit here to implement your code
    sol = []
    
    
    A = LUdecomp(A)
    b = LUsolve(A,b)
    
    sol = b    
    

    return list(sol)
    
#============ Omega Optimal ================

def omega_Optimal(A):
    
    #print('This is eigen values \n============')
    eigen = np.linalg.eigvals(A)
    #print(eigen)
    
    #print('\n\nThis is eigen arrays\n=============')
    #reshape_eig = np.reshape(eigen, (-1))
    #array_eig = np.asarray(np.reshape(eigen, (-1,0)))
    #print(array_eig)
    
    #print('\n\nTest the value to be Real Number \n==========')
    #real_eigen = np.all(eigen)
    #print(real_eigen)
    
    real_eigen = []
    
    for num in eigen:
        if(not(np.iscomplex(num))):
            real_eigen.append(num)
            
    #print(real_eigen)
    
    #print('\n\nThis is the highest value of eigen \n=================')
    max_eig = max(real_eigen)
    max_eig = np.real(max_eig)
    print('MAX_EIG')
    print(max_eig)
    #print(max_eig)
    
    if( (1-np.power(max_eig,2)) > 1 ):
        omega = ( 2 * (1 - np.sqrt(1-np.power(max_eig,2))) ) / np.power(max_eig,2)
    else:
        omega = -1
    
    print('\n\nThis is Omega \n=======================')
    print(omega) 
    
    return omega
    
#===========================================

#============SOR method start ================
def sor(A, b):
    # Edit here to implement your code    
    ITERATION_LIMIT = 200    
    
    omega = omega_Optimal(A)
    
    sol = []

#    omega = 0.2
#    A = np.array([[ 2, -1,  0], 
#                  [-1,  3, -1],
#                  [ 0, -1,  2]]).astype(float)
#    b = np.array([1,8,-5]).astype(float)
    x = np.zeros_like(b)

    msg  = '  i          x(1)         x(2)          x(3) \n'
    msg += '=============================================\n'
    msg += '%3d  %12.4f  %12.4f  %12.4f\n'%(0, x[0],x[1],x[2])
    for itr in range(ITERATION_LIMIT):
        for i in range(len(b)):
            sums = np.dot( A[i,:], x )
            x[i] = x[i] + omega*(b[i]-sums)/A[i,i]
        msg += '%3d  %12.4f  %12.4f  %12.4f\n'%(itr, x[0],x[1],x[2])
        
    for num in x:
        sol.append(num)
#    sol.append(x[0])
#    sol.append(x[1])
#    sol.append(x[2])
    #sol.append(x[3])

    return list(sol)
    
#============SOR method END ================
#1303042    

def solve(A, b):

    condition = False # State and implement your condition here
    
    omega = omega_Optimal(A)
    
    if(omega == -1):
        print('Optimal Omega unable to calculate as Sqaure root of (1 - K^2) < 0')
        condition = True
    else:
        print('Omega is %f'%omega)
        condition = False
    
    if condition:
        print('Solve by lu(A,b)')
        return lu(A,b)
    else:
        print('Solve by sor(A,b)')
        return sor(A,b )

if __name__ == "__main__":
    ## import checker
    ## checker.test(lu, sor, solve)
    
    A = [[2,1,6], [8,3,2], [1,5,1]]
    b = [9, 13, 7]
    A = np.array(A).astype(float) 
    b = np.array(b).astype(float)         
    flag = False
    
    sol = solve(A, b)
    
    print(sol)
    print('=======END OF FIRST DEMENSION ANSWER ============\n\n')
    
    
    A = [[6566, -5202, -4040, -5224, 1420, 6229],
         [4104, 7449, -2518, -4588,-8841, 4040],
         [5266,-4008,6803, -4702, 1240, 5060],
         [-9306, 7213,5723, 7961, -1981,-8834],
         [-3782, 3840, 2464, -8389, 9781,-3334],
         [-6903, 5610, 4306, 5548, -1380, 3539.]]
    b = [ 17603,  -63286,   56563,  -26523.5, 103396.5, -27906]
    A = np.array(A).astype(float)
    b = np.array(b).astype(float) 
    
    
    sol = solve(A,b)
    print(sol)
    print('=======END OF SECOND DEMENSION ANSWER ============\n\n')
    
    
