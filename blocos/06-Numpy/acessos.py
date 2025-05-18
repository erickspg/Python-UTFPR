import numpy as np

array1 = np.array([1, 6, 9, 15, 20])
#print(array1)
#print("Terceiro elemento do array: {}".format(array1[2]))

array2 = np.array([[90, 120, 180], [32, 58, 11], [5, 0, 552]])
print("Segunda linha e terceira coluna: {}".format(array2[1][2]))
print("Último elemento da última linha: {}".format(array2[-1][-1]))

array3 = np.array([1, 6, 9, 15, 20])
print("Terceiro ao quinto elemento do array1: {}".format(array3[2:5]))

array4 = np.array([[90, 120, 180], [32, 58, 11], [5, 0, 552], [19, 66, 202]])
print("1ª até 2ª linha do array:\n{}".format(array4[1:3]))
print("1ª até 2ª linha, somente terceira coluna: {}".format(array4[1:3, 2]))