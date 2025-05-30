#EXECUTAR NO COLLAB
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# Parâmetros
NUM_CIDADES = 20
POP_SIZE = 100
NUM_GERACOES = 200
TAXA_MUTACAO = 0.01
ELITE_SIZE = 5

# Gerar cidades aleatórias
cidades = np.random.rand(NUM_CIDADES, 2)

def distancia(p1, p2):
    return np.linalg.norm(p1 - p2)

def fitness(rota):
    return -sum(distancia(cidades[rota[i]], cidades[rota[(i + 1) % NUM_CIDADES]]) for i in range(NUM_CIDADES))

def selecao(pop, scores):
    idx = np.random.choice(len(pop), 5, replace=False)
    return pop[max(idx, key=lambda i: scores[i])]

def crossover(p1, p2):
    a, b = sorted(np.random.choice(NUM_CIDADES, 2, replace=False))
    child = [-1] * NUM_CIDADES
    child[a:b] = p1[a:b]
    p2_rest = [city for city in p2 if city not in child]
    ptr = 0
    for i in range(NUM_CIDADES):
        if child[i] == -1:
            child[i] = p2_rest[ptr]
            ptr += 1
    return child

def mutacao(individuo):
    if np.random.rand() < TAXA_MUTACAO:
        a, b = np.random.choice(NUM_CIDADES, 2, replace=False)
        individuo[a], individuo[b] = individuo[b], individuo[a]
    return individuo

populacao = [np.random.permutation(NUM_CIDADES).tolist() for _ in range(POP_SIZE)]

# Preparar visualização
fig, ax = plt.subplots()
linha, = ax.plot([], [], 'o-', lw=2)
melhores_texto = ax.text(0.02, 1.02, '', transform=ax.transAxes)

def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return linha, melhores_texto

def evoluir(i):
    global populacao

    scores = [fitness(ind) for ind in populacao]
    nova_pop = []

    elite_idx = np.argsort(scores)[-ELITE_SIZE:]
    elite = [populacao[i] for i in elite_idx]
    nova_pop.extend(elite)

    while len(nova_pop) < POP_SIZE:
        pai1 = selecao(populacao, scores)
        pai2 = selecao(populacao, scores)
        filho = crossover(pai1, pai2)
        filho = mutacao(filho)
        nova_pop.append(filho)

    populacao = nova_pop

    best_idx = np.argmax(scores)
    best_route = populacao[best_idx]
    route_coords = np.append(cidades[best_route], [cidades[best_route[0]]], axis=0)

    linha.set_data(route_coords[:, 0], route_coords[:, 1])
    melhores_texto.set_text(f"Geração {i + 1}, Distância: {-fitness(best_route):.4f}")
    return linha, melhores_texto

ani = animation.FuncAnimation(fig, evoluir, frames=NUM_GERACOES,
                              init_func=init, blit=True, interval=100, repeat=False)

# Salvar como vídeo e exibir no Colab
from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=10)

HTML(ani.to_jshtml())