import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 5.0, 100)
y = np.exp(-x)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_xlabel('Tempo')
ax.set_ylabel('Quantidade')
ax.set_title('Crescimento')
ax.grid(True) # setando false remove as linhas guias do grid

plt.show()