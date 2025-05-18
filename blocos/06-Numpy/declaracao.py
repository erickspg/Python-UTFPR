import numpy as np

#list/tupla sao convertidos para array
ar_exemplo = np.array([1 , 2 , 3 , 4 , 5])
print(ar_exemplo)
print(type(ar_exemplo))

arr_0_dimensoes = np.array(68)
arr_1_dimensoes = np.array([1, 6, 9, 15, 20])
arr_2_dimensoes = np.array([[90, 120, 180], [32, 58, 11], [5, 0, 552]])

#numero de dimensoes de cada array
print(arr_0_dimensoes.ndim)
print(arr_1_dimensoes.ndim)
print(arr_2_dimensoes.ndim)