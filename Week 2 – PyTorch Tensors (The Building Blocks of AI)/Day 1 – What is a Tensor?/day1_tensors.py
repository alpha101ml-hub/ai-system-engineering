'''
What is a tensor?
A tensor is just a container for numbers - like a list, but more powerful. It can have multiple dimensions:
- 0D tensor: A single number (scalar) -> 42
- 1D tensor: A list of numbers (vector) -> [1,2,3]
- 2D tensor: a table of numbers (matrix) -> [[1,2], [3,4]]
- 3D tensor: A cube of numbers -> multiple tables stacked together


Why deos AI use tensors?
- Images are 3D tensors (height x width x colour channels)
- Text is 1D tensors (sequence of words)
- Neural networks process everything as tensors
'''

import torch

print("--- CREATING TENSORS ---")

# 1. From a Python list
list_data = [1,2,3,4,5]
tensors_from_list = torch.tensor(list_data)
print("Tensor from list:", tensors_from_list)

# 2. A 2D tensor (matrix)
matrix_data = [[1,2,3], [4,5,6]]
tensor_2d = torch.tensor(matrix_data)
print("2D tensor:\n", tensor_2d)

# 3. Tensor of zeros
zeros_tensor = torch.zeros(3, 4)  # 3 rows, 4 columns
print("Zeros tensor:\n", zeros_tensor)

# 4. Tensor of ones
ones_tensor = torch.ones(2,3) # 2 rows , 3 columns
print("Ones tensor:\n", ones_tensor)

# 5. Random tensor
random_tensor = torch.rand(2,2) # 2x2 random numbers between 0 and 1
print("Random tensor:\n", random_tensor)


print("\n--- TENSOR SHAPE ---")
print("Shape of list tensor:", tensors_from_list.shape)
print("Shape of 2D tensor:", tensor_2d.shape)
print("Shape of zeros tensor:", zeros_tensor.shape)
print("Shape of ones tensor:", ones_tensor.shape)

# shape is a tuple (rows, columns) for 2D tensors

print("\n--- TENSOR OPERATIONS ---")

a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])

# Addition
print("a + b =", a + b)

# Subtraction
print("a - b =", a - b)

# Multiplication (element-wise)
print("a * b =", a * b)

# Division
print("b / a =", b / a)

# Scalar operations (with a single number)
print("a * 2 =", a * 2)
print("a + 10 =", a + 10)



print("\n--- INDEXING AND SLICING ---")

matrix = torch.tensor([[1, 2, 3], 
                       [4, 5, 6], 
                       [7, 8, 9]])

print("Original matrix:\n", matrix)

# Access a single element
print("Element at row 1, column 1:", matrix[0, 0])  # First row, first column
print("Element at row 2, column 3:", matrix[1, 2])  # Second row, third column

# Access a whole row
print("First row:", matrix[0, :])  # row 0, all columns
print("Second row:", matrix[1, :])

# Access a whole column
print("First column:", matrix[:, 0])  # all rows, column 0
print("Last column:", matrix[:, -1])  # all rows, last column

# Slice a sub-matrix
print("Top-left 2x2:\n", matrix[0:2, 0:2])

'''
matrix[0, 0]  first row, first column (zero-based indexing)

matrix[1, 2]  second row, third column

matrix[0, :]  first row, all columns

matrix[:, 1]  all rows, second column

matrix[0:2, 0:2]  rows 0 to 1, columns 0 to 1
'''
