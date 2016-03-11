UECM3033 Assignment #2 Report
========================================================

- Prepared by: Tee Yeh Hun
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/Yehhun/UECM3033_assign2](https://github.com/Yehhun/UECM3033_assign2)

Explain your selection criteria here.

We can use LU decomposition for both matrix.We need to confirm that the matrix is definite matrix to use SOR with correct variable.
We need also to made all the p(Kj) which is our eigenvalue smaller than 1 in order to get omega value. 

Explain how you implement your `task1.py` here.

For the first 3x3 matrix, I am able to use LU decomposition to solve it, then when using SOR method, I found out that the equation p(Kj) is more than one, so I am unable to find optimal omega. That why it is unable to use SOR method. For 6*6 matrix, I am able to find out using LU decomposition method.In SOR method, I am able to find out p(Kj) but unable to get the right answer.This is because only one eigenvalue real number  is 0.98 and other eigenvalue are imaginary number.That the reason we cannot use SOR for 6x6.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Lenna.png)

![2_Picture.png](2_Picture.jpg)

How many non zero element in $\Sigma$?

The number of none zero in Sigma is 700.

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

We generate by splitting the original picture to green, blue and red. After than we use smaller matrix to combine it to become lower resolution.

Lower resolution

![lowerresolution.png](lowerresolution.png)

Better resolution

![higherresolution.png](higherresolution.png)

Each RGB colour picture is being given and the matrix is then used to decomposite using SVD.

The implement of task2 is mainly using scipy.linalg library which contains method, svd to calculate the Sigma, U and V.

By keeping only certain none-numbers in the U, it will construct a lower resolution matrix when multiply the SVD. 

The Multiply of SVD would then return back the orginal matrix. And thus, returning back an image according to the matrix. 

When dealing with dimension of none square picture, it is noted that the product of Matrix required to have the number of column in first matrix to be equal as number of row in second matrix to work. (Sigma, U and V)

By adding the RGB matrix using method numpy.stack, we will able to display the colour image but with lesser resolution. 

What is a sparse matrix? 

A sparse matrix is a matrix in which most of the elements are zero. By contrast, if most of the elements are nonzero, then the matrix is considered dense. The fraction of non-zero elements over the total number of elements  in a matrix is called the sparsity.

-----------------------------------

<sup>last modified: 11-3-2016 </sup>
