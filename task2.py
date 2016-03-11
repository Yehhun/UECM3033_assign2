

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import cv2
import numpy as np
import matplotlib
from scipy import linalg
from PIL import Image

matplotlib.rcParams['backend'] = "Qt4Agg"


img=mpimg.imread('2_Picture.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
#plt.show()


#This function is call to count number of NONE-ZERO in singular values of (M,N)
def countNotZero(numList):
    count = 0
    for num in numList:
        if num != 0:
            count +=1
    return count
    
def takeNotZero(numList,numTake):
    count = 0
    newList = []
    for num in numList:
        if(count<numTake):
            newList.append(num)
            count += 1
        else:
            newList.append(0)
    print(count)
    return newList
    
def compositeSVD(U, s, Vh):
    newList = []
    newList = np.matrix.dot(U, np.matrix.dot(np.diag(s), Vh))
    return newList;
        


#This is Red Image

U, s, Vh = linalg.svd(r,full_matrices=True) #SVD method
'''
print('Following shown the singular values (M,N) \n =====================================')
print(s) #The singular values, sorted in non-increasing order. Of shape (K,), with K = min(M, N).
print('==========================================\n\n')
print('==========================================\nUnitary Matrix left singular vectors (M,M)\n==========================================')
print(U) #Unitary matrix having left singular vectors as columns. Of shape (M,M) or (M,K), depending on full_matrices.
print('\n==========================================\n')
print('Unitary Matrix Right singular vectors (N,N)\n')
print('============================================\n')
print(Vh) #Unitary matrix having right singular vectors as rows. Of shape (N,N) or (K,N) depending on full_matrices.
print('==========END OF LINE (RED)=======================\n')
#count = 0
#for num in s:
#    if num != 0:
#        count +=1
print('The number of "none-zero" for Red are %d'%countNotZero(s))
'''
#Resize so that Matrix Product is allowed
print(U.shape)
print(s.shape)
print(Vh.shape)

U.resize((800,1000))
s.resize(1000)
print(s.shape)
print(U.shape)
###Composite Back into Red Image
print('=======Composite Back Red Image ================\n')


r2 = compositeSVD(U,s,Vh)

fig2 = plt.figure(2)
ax5 = fig2.add_subplot(1,1,1)
ax5.imshow(r2, cmap = 'Reds')
plt.show()
print('======END OF RED COMPOSITE BACK RED IMAGE=====\n')

#Take num and append to new List
s_take = takeNotZero(s,30)
s_take200 = takeNotZero(s,200)
#print(s_take)

r3 = compositeSVD(U,s_take,Vh)
r200 = compositeSVD(U,s_take200,Vh)
    
fig3 = plt.figure(1)
ax6 = fig3.add_subplot(1,1,1)
ax6.imshow(r3, cmap = 'Reds')
plt.show()
print('=====SHOULD BE COMPRESSED RED IMAGE======\n')

#END OF take num for RED
'''
#print(s[510])
#print(s[511])
#print(s[509])
#print(s[508])
#print(s[507])
#if s[508] == s[509]:
#    print('508 and 509 are the same')
#else:
#    print('There are not the same')
'''

#This is Green Image

U, s, Vh = linalg.svd(g) #SVD method
'''
print('Following shown the singular values (M,N) \n =====================================')
print(s) #The singular values, sorted in non-increasing order. Of shape (K,), with K = min(M, N).
print('==========================================\n\n')
print('==========================================\nUnitary Matrix left singular vectors (M,M)\n==========================================')
print(U) #Unitary matrix having left singular vectors as columns. Of shape (M,M) or (M,K), depending on full_matrices.
print('\n==========================================\n')
print('Unitary Matrix Right singular vectors (N,N)\n')
print('============================================\n')
print(Vh) #Unitary matrix having right singular vectors as rows. Of shape (N,N) or (K,N) depending on full_matrices.
print('==========END OF LINE (GREEN)=======================\n')
print('The number of "none-zero" for Green are %d'%countNotZero(s))
'''
#Resize so that Matrix Product is allowed
U.resize((800,1000))
s.resize(1000)

#Take num and append to new List
s_take = takeNotZero(s,30)
s_take200 = takeNotZero(s,200)
#print(s_take)

g3 = compositeSVD(U,s_take,Vh)
g200 = compositeSVD(U,s_take200,Vh)
    
fig3 = plt.figure(1)
ax6 = fig3.add_subplot(1,1,1)
ax6.imshow(g3, cmap = 'Greens')
plt.show()
print('=====SHOULD BE COMPRESSED Green IMAGE======\n')

#This is Blue Image

U, s, Vh = linalg.svd(b) #SVD method
'''
print('Following shown the singular values (M,N) \n =====================================')
print(s) #The singular values, sorted in non-increasing order. Of shape (K,), with K = min(M, N).
print('==========================================\n\n')
print('==========================================\nUnitary Matrix left singular vectors (M,M)\n==========================================')
print(U) #Unitary matrix having left singular vectors as columns. Of shape (M,M) or (M,K), depending on full_matrices.
print('\n==========================================\n')
print('Unitary Matrix Right singular vectors (N,N)\n')
print('============================================\n')
print(Vh) #Unitary matrix having right singular vectors as rows. Of shape (N,N) or (K,N) depending on full_matrices.
print('==========END OF LINE (BLUE)=======================\n')
print('The number of "none-zero" for blue are %d'%countNotZero(s))
'''
#Resize so that Matrix Product is allowed
U.resize((800,1000))
s.resize(1000)

#Take num and append to new List
s_take = takeNotZero(s,30)
s_take200 = takeNotZero(s,200)
#print(s_take)

b3 = compositeSVD(U,s_take,Vh)
b200 = compositeSVD(U,s_take200,Vh)
    
fig3 = plt.figure(1)
ax6 = fig3.add_subplot(1,1,1)
ax6.imshow(g3, cmap = 'Blues')
plt.show()
print('=====SHOULD BE COMPRESSED Blue IMAGE======\n')

print('=====COMPRESSED RGB IMAGE (take 30 none zero)=========\n')
#rgbArray = (np.dstack((r3,g3,b3))* 255.999).astype(np.uint8)
rgbArray = np.dstack((r3,g3,b3)).astype(np.uint8)
#rgbArray = Image.fromarray(np.uint8(rgb*255.999))
#rgbArray = np.zeros((512,512,3), 'uint8')
#rgbArray[..., 0] = r*256
#rgbArray[..., 1] = g*256
#rgbArray[..., 2] = b*256
img = Image.fromarray(rgbArray)
img.save('CompressedColor.jpeg')
fig4 = plt.figure(1)
ax7 = fig4.add_subplot(1,1,1)
ax7.imshow(rgbArray)
plt.show()

print('=====END OF COMPRESSED RGB IMAGE (take 30 none zero)=========\n')

print('=====COMPRESSED RGB IMAGE (take 200 none zero)=========\n')
#rgbArray = (np.dstack((r3,g3,b3))* 255.999).astype(np.uint8)
rgbArray2 = np.dstack((r200,g200,b200)).astype(np.uint8)
#rgbArray = Image.fromarray(np.uint8(rgb*255.999))
#rgbArray = np.zeros((512,512,3), 'uint8')
#rgbArray[..., 0] = r*256
#rgbArray[..., 1] = g*256
#rgbArray[..., 2] = b*256
img = Image.fromarray(rgbArray2)
img.save('CompressedColor.jpeg')
fig5 = plt.figure(1)
ax8 = fig5.add_subplot(1,1,1)
ax8.imshow(rgbArray2)
plt.show()

print('=====END OF COMPRESSED RGB IMAGE (take 200 none zero)=========\n')