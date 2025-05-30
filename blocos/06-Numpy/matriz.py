import numpy as np

# Operações com matriz A
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Diagonal principal:\n{}".format(np.diagonal(A)))
print("Diagonal reversa:\n{}".format(np.fliplr(A).diagonal()))
print("Matriz transposta:\n{}".format(np.transpose(A)))

# Operações aritmeticas entre A e B
c_sum = A + B
print("Soma:\n{}".format(c_sum))

c_multiply = A * B
print("Multiplicação elemento a elemento:\n{}".format(c_multiply))

c_matmul = np.matmul(A, B)
print("Multiplicação matricial:\n{}".format(c_matmul))