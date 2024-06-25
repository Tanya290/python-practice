
#NumPy is a powerful library in Python for numerical computing. It provides support for arrays, matrices, and many mathematical functions to operate on these data structures. 

#NumPy is a versatile library that is fundamental for scientific computing in Python. Its powerful features for array manipulation, mathematical operations, and linear algebra make it essential for data analysis, machine learning, and other computational tasks.



#Core Features
#1. ndarray: The primary data structure in NumPy is the ndarray, a multidimensional array.
#2. Element-wise Operations: NumPy supports element-wise operations on arrays.
#3. Broadcasting: Operations on arrays of different shapes.
#4. Universal Functions (ufuncs): Functions that operate element-wise on arrays.
#5. Linear Algebra: Functions for linear algebra operations.
#6. Rndom Sampling: Functions for generating random numbers.
#7. Fourier Transforms: Functions for performing Fourier transforms.
#8. Polynomials: Functions for polynomial operations.
#9. Statistics: Statistical functions.
#10.Array Manipulation: Functions for reshaping, stacking, and splitting arrays.


#Commonly Used Functions

#Array Creation
#- `numpy.array()`: Create an array.
#- `numpy.zeros()`: Create an array filled with zeros.
#- `numpy.ones()`: Create an array filled with ones.
#- `numpy.full()`: Create an array filled with a specified value.
#- `numpy.eye()`: Create an identity matrix.
#- `numpy.linspace()`: Create an array with evenly spaced values.
#- `numpy.arange()`: Create an array with a range of values.

#Array Attributes
#- `ndarray.shape`: Shape of the array.
#- `ndarray.size`: Number of elements.
#- `ndarray.ndim`: Number of dimensions.
#- `ndarray.dtype`: Data type of the elements.

#Array Manipulation
#- `numpy.reshape()`: Change the shape of an array.
#- `numpy.flatten()`: Flatten a multi-dimensional array into one dimension.
#- `numpy.transpose()`: Transpose the array.
#- `numpy.concatenate()`: Concatenate arrays along an axis.
#- `numpy.hstack()`: Stack arrays horizontally.
#- `numpy.vstack()`: Stack arrays vertically.

#Element-wise Operations
#- `numpy.add()`, `numpy.subtract()`, `numpy.multiply()`, `numpy.divide()`: Basic arithmetic operations.
#- `numpy.exp()`, `numpy.log()`, `numpy.sqrt()`, `numpy.power()`: Exponential, logarithm, square root, and power functions.
#- `numpy.sin()`, `numpy.cos()`, `numpy.tan()`: Trigonometric functions.
#- `numpy.maximum()`, `numpy.minimum()`: Maximum and minimum functions.

#Statistical Functions
#- `numpy.mean()`: Mean of the array elements.
#- `numpy.median()`: Median of the array elements.
#- `numpy.std()`: Standard deviation.
#- `numpy.var()`: Variance.
#- `numpy.sum()`: Sum of the array elements.
#- `numpy.min()`, `numpy.max()`: Minimum and maximum values.

#Linear Algebra
#- `numpy.dot()`: Dot product of two arrays.
#- `numpy.matmul()`: Matrix multiplication.
#- `numpy.linalg.inv()`: Inverse of a matrix.
#- `numpy.linalg.det()`: Determinant of a matrix.
#- `numpy.linalg.eig()`: Eigenvalues and eigenvectors.

#Random Sampling
#- `numpy.random.rand()`: Random values in a given shape.
#- `numpy.random.randn()`: Random values from the standard normal distribution.
#- `numpy.random.randint()`: Random integers.
#- `numpy.random.choice()`: Random samples from a given array.

#Fourier Transforms
#- `numpy.fft.fft()`: Compute the one-dimensional discrete Fourier Transform.
#- `numpy.fft.ifft()`: Compute the one-dimensional inverse discrete Fourier Transform.

#Polynomials
#- `numpy.poly1d()`: A one-dimensional polynomial class.
#- `numpy.polyval()`: Evaluate a polynomial at specific values.
#- `numpy.polyfit()`: Least squares polynomial fit.


#Examples

#1.Array Creation:

import numpy as np
arr = np.array([1, 2, 3])
   
#2.Array Manipulation:

arr = np.arange(10)
reshaped_arr = arr.reshape((2, 5))


#3.Element-wise Operation:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.add(a, b)  # array([5, 7, 9])


#4.Statistical Functions:
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)  # 3.0


#5.Linear Algebra:

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)



#Array Indexing and Slicing

#Indexing
#Indexing allows you to access individual elements or subsets of an array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# Accessing single elements
print(arr[0])  # Output: 1
print(arr[-1]) # Output: 5

# For multi-dimensional arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[0, 1])  # Output: 2
print(arr2d[1, -1]) # Output: 6


#Slicing
#Slicing allows you to access a range of elements in an array.

arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # Output: [2, 3, 4]
print(arr[:3])   # Output: [1, 2, 3]
print(arr[::2])  # Output: [1, 3, 5]

# For multi-dimensional arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[:, 1])    # Output: [2, 5]
print(arr2d[1, 1:])   # Output: [5, 6]
print(arr2d[1:, ::2]) # Output: [[4, 6]]


#NumPy Data Types

#NumPy supports a variety of data types for its arrays. These include:
#- Integer types: `np.int8`, `np.int16`, `np.int32`, `np.int64`
#- Unsigned integer types: `np.uint8`, `np.uint16`, `np.uint32`, `np.uint64`
#- Floating-point types: `np.float16`, `np.float32`, `np.float64`
#- Complex types: `np.complex64`, `np.complex128`
#- Boolean type: `np.bool_`
#- Object type: `np.object_`
#- String type: `np.str_`

#Example:
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.dtype)  # Output: int32

#Copy vs. View

#When you create a new array from an existing one, NumPy may either copy the data (a true copy) or create a view (a new array object that looks at the same data).

#Copy
#A copy creates a new array with its own data.

arr = np.array([1, 2, 3])
arr_copy = arr.copy()
arr_copy[0] = 10
print(arr)       # Output: [1, 2, 3]
print(arr_copy)  # Output: [10, 2, 3]


#View
#A view is a new array object that shares the same data with the original array.


arr = np.array([1, 2, 3])
arr_view = arr.view()
arr_view[0] = 10
print(arr)       # Output: [10, 2, 3]
print(arr_view)  # Output: [10, 2, 3]


#Array Shape and Reshape

#Shape
#The shape of an array is a tuple that indicates the size of the array in each dimension.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)


#Reshape
#Reshape changes the shape of an array without changing its data.

arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshaped = arr.reshape((2, 3))
print(arr_reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]


#Array Iterating

#You can iterate over arrays using loops.

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2d:
    for y in x:
        print(y)

#Array Join, Split, Search, Sort, and Filter

#Join
#Joining arrays can be done using functions like `np.concatenate()`, `np.vstack()`, and `np.hstack()`.


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
joined_arr = np.concatenate((arr1, arr2))
print(joined_arr)  # Output: [1, 2, 3, 4, 5, 6]


#Split
#Splitting arrays can be done using functions like `np.split()`, `np.hsplit()`, and `np.vsplit()`.


arr = np.array([1, 2, 3, 4, 5, 6])
splitted_arr = np.split(arr, 3)
print(splitted_arr)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]


#Search
#Searching within arrays can be done using functions like `np.where()`, `np.nonzero()`, and `np.argmax()`.


arr = np.array([1, 2, 3, 4, 5, 6])
indices = np.where(arr > 3)
print(indices)  # Output: (array([3, 4, 5]),)


#Sort
#Sorting arrays can be done using `np.sort()`

arr = np.array([3, 1, 2])
sorted_arr = np.sort(arr)
print(sorted_arr)  # Output: [1, 2, 3]


#Filter
#Filtering arrays can be done using boolean indexing.


arr = np.array([1, 2, 3, 4, 5, 6])
filtered_arr = arr[arr > 3]
print(filtered_arr)  # Output: [4, 5, 6]


#Summary
#NumPy provides powerful tools for numerical computing in Python. From array creation, indexing, and slicing to more advanced operations like reshaping, joining, splitting, searching, sorting, and filtering, NumPy is essential for data manipulation and analysis in Python.