# import the "numpy" library
import numpy as np

# Organization of numpy array
python_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]            # python array
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # numpy array
print("Python list:", python_list)
print("Numpy array:", numpy_array)

# Finding the size of the array
numpy_array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Numpy array size:", numpy_array1.ndim)

# Finding the number of rows and columns of the array
numpy_array2 = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
print("Numpy array of rows size and columns size",numpy_array2.shape)

# Changing the number of rows and columns of an array
# (Note: The original matrix and the reshaped matrix must have the same number of elements.)
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("",numpy_array.reshape(1,10))      #Resizing for (1,10)
print("",numpy_array.reshape(5,2))       #Resizing for (5,2)

# Creating a numpy array containing the numbers starting from the specified starting value and increasing
# by the number of steps each time, up to the ending value. (np.arange(start, end, number of steps))
print(np.arange(0,10,3))

# Selecting the elements of the array (ndarray[rows,columns])
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(5,2)
first_row = numpy_array[0]
print("First row",first_row)
first_column = numpy_array[:,0]
print("First column",first_column)

# Reverse the array
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(5,2)
print(numpy_array)
print("Reverse array:\n",numpy_array[::-1])

# Generating 0 matrix : np.zeros()
print(np.zeros((5,4)))

# Generating matrix 1: np.ones()
print(np.ones((3,3,3)))

# Creating a identity matrix): np.eye()
print(np.eye(4))       # 4x4 identity matrix

# Combining matrices
numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(5,2)
print(np.concatenate([numpy_array, numpy_array], axis =0))     #Row-based concatenation
print(np.concatenate([numpy_array, numpy_array], axis =1))     #Column-based concatenation

# Calculating sum, max and min values
numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(5,2)
print(numpy_array.max())
print(numpy_array.min())
print(numpy_array.sum())
print(numpy_array.sum(axis = 1))      #Sum of rows

# Calculate mean, median, variance and standard deviation
numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
print(numpy_array.mean())        #mean
print(np.median(numpy_array))    #median
print(numpy_array.var())         #variance
print(numpy_array.std())         #standard deviation

# Arithmetic operations on matrices
numpy_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(3,3)
print("My numpy array:\n",numpy_array)
print(numpy_array + numpy_array)
print(numpy_array - numpy_array)
print(numpy_array * numpy_array)
print(numpy_array / numpy_array)
print(numpy_array + 2)

# Operations with special functions
numpy_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(3,3)
print(np.sin(numpy_array))
print(np.cos(numpy_array))
print(np.sqrt(numpy_array))
print(np.exp(numpy_array))
print(np.log(numpy_array))

# Multiplication of matrices
numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array1 = numpy_array.reshape(5,2)
numpy_array2 = numpy_array.reshape(2,5)
print(np.dot(numpy_array1,numpy_array2))

# Transpose of the matrix
numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
numpy_array = numpy_array.reshape(5,2)
print(numpy_array)
print(numpy_array.T)

# Working with Conditional Expressions in Numpy
numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
boolean_array = numpy_array >= 5
print(boolean_array)














