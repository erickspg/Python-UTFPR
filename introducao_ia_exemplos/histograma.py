import matplotlib.pyplot as plt
import numpy as np

n_points = 100000
n_bins = 20
rng = np.random.default_rng(1000)

#gerar as distribuicoes
dist = rng.standard_normal(n_points)
#criar a imagem
fig, ax = plt.subplots()

#colocar na imagem os dados
ax.hist(dist, bins=n_bins)
ax.set_xlabel('Intervalos')
ax.set_ylabel('Ocorrências')
ax.set_title('Histograma')

plt.show()