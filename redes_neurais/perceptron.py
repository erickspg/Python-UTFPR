from sklearn import preprocessing # biblioteca para suporte ao pré-processamento
from sklearn.model_selection import train_test_split # biblioteca para separação de amostras para treino e teste
from sklearn.linear_model import Perceptron # biblioteca com funções para a execução da RNA Perceptron
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import metrics # biblioteca para obtenção de métricas para avaliação dos modelos
import matplotlib.pyplot as plt # biblioteca para plotar gráfico
from matplotlib.colors import ListedColormap #personalizar cores do gráfico
import numpy as np
import pandas as pd
import random # biblioteca aplicada na geração de números randômicos
#from google.colab import drive
#drive.mount('/content/drive') # Montando o Google Drive na mesma conta do Google Colab

# Caminho do dataset 
df = pd.read_csv("/content/drive/MyDrive/DataSets/bancario.csv") #AJUSTAR PARA CAMINHO LOCAL
#print(df)

# Obtendo valores da coluna classe
y = df['Classe'].values
# substituindo o valor string em numérico, baseado no que determina a função de ativação
y = np.where(y == 'mau', -1, 1)
# separando as colunas com as variáveis do dataset para determinar os inputs da RNA
X = df.iloc[:, [1,2]].values

#print(y.shape)
#print(X.shape)

# normalização dos dados sklearn - dados entre 0 e 1 -
scaler = preprocessing.MinMaxScaler()
X = scaler.fit_transform(X)

# plotando o gráfico para verificação se as amostras são linearmente separáveis
plt.scatter(X[:,1],X[:,0],c=y)
plt.title("Setosa x versicolor" )
plt.xlabel('Sepal.Width')
plt.ylabel('Sepal.Length')
plt.show


# separação do dataset em amostras para treino e teste, considerando 30% dos valores para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=12)
#print(X_train.shape)
#print(X_test.shape)

#treinando modelo
p = Perceptron(random_state=42, eta0=0.0001, alpha=0.1)
p.fit(X_train, y_train)

#Validando as amostrar do treinamento
predictions_train = p.predict(X_train) # validação do conjunto de amostras treinadas
train_score = accuracy_score(predictions_train, y_train) # avaliação de acurácia da classificação das amostras que foram apresentadas no treinamento
print("Acurácia com dados de treinamento: ", train_score)

predictions_test = p.predict(X_test) # validação do conjunto de amostras que não participaram do treinamento
test_score = accuracy_score(predictions_test, y_test) # avaliação de acurácia da classificação das amostras que foram apresentadas no treinamento
print("Acurácia com dados de teste: ", test_score)

print(classification_report(predictions_test, y_test))

print("Número de épocas no treinamento: ", p.n_iter_)
print("Lista de parâmetros configurados na Perceptron: ", p.get_params())

# Apresentação gráfica da matriz de confusão dos testes classificados
conf_matrix = confusion_matrix(y_test, predictions_test)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels = ['Setosa', 'Versicolor'])
cm_display.plot()
plt.show()

# Teste individual de amostras já normalizadas
A = np.array([0.4329,-1.3719,0.7022,-0.8535]) # Padrão correto = 1
A_y = np.array([1])
B = np.array([-0.3024,-0.2286,-0.8630,-2.7909]) # Padrão correto = -1
B_y = np.array([-1])

prediction_A = p.predict([A])
prediction_B = p.predict([B])
print("Acurácia com dados de A: ", accuracy_score(prediction_A, A_y))
print("Acurária com dados de B: ", accuracy_score(prediction_B, B_y))