import numpy as np
from scipy import io
from scipy import special
from scipy import linalg
from scipy.linalg import inv
from scipy.linalg import eig
from scipy.sparse import coo_matrix, csr_matrix

array = np.ones((4, 4))
io.savemat('test.text', {'array': array})
data = io.loadmat('test.text')
print(data['array'])


values = [27, 64, 891]
for val in values:
    print(f"Cubic root of {val} is {special.cbrt(val)}")



matrix = np.array([[4, 5],[3, 2]])
det = linalg.det(matrix)
print(f"Determinant of the matrix is: {det}")



A = np.array([[1, 2, 3],[0, 4, 5],[1, 0, 6]])
A_inv = inv(A)
print("Original Matrix:")
print(A)
print("\nInverse Matrix:")
print(A_inv)


A = np.array([[5, 4], [6, 3]])
eigenvalues, eigenvectors = eig(A)
print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)




# Create sparse matrix A in COO format
row = np.array([0, 0, 1, 2])
col = np.array([0, 2, 1, 2])
data = np.array([1, 2, 3, 4])
A = coo_matrix((data, (row, col)), shape=(3, 3))
print("Matrix A (COO format) as dense array:")
print(A.toarray())

# Create sparse matrix B in CSR format
B = csr_matrix([[0, 5, 0], [0, 0, 6], [7, 0, 0]])
print("\nMatrix B (CSR format) as dense array:")
print(B.toarray())

# Analyze various functions
print("\nSum of non-zero elements in A:", A.sum())
print("Sum of non-zero elements in B:", B.sum())

# Element-wise multiplication
C = A.multiply(B)
print("\nElement-wise multiplication (A * B) as dense array:")
print(C.toarray())

# Matrix addition
D = A + B
print("\nMatrix addition (A + B) as dense array:")
print(D.toarray())

# Matrix multiplication
E = A.dot(B.toarray())
print("\nMatrix multiplication (A @ B) as dense array:")
print(E)

# Transpose of A
A_transpose = A.transpose()
print("\nTranspose of A as dense array:")
print(A_transpose.toarray())