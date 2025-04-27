#Rede neural para reconhecimento de caracteres
import tensorflow as tf

#dataset mnist - 60 mil figuras 28x28 pixels
mnist = tf.keras.datasets.mnist

#carregar os dados de treino e teste
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#normalizacao dos dados (figuras) - (invervalo sempre 0 - 255) - vamos fazer intervalo ficar (0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

#criar uma rede neural
model = tf.keras.models.Sequential([
    #Entrada tem que ser transformada de figuras 28x28 em um vetor
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    #camada oculta com N neuronios utilizando a funcao de ativacao reLU
    tf.keras.layers.Dense(64, tf.nn.relu),
    # camada oculta tem X% dos neuronios ativados aleatoriamente
    tf.keras.layers.Dropout(0.2),
    #Camada de saída - como são números de 0 a 9 serão 10 saídas
    tf.keras.layers.Dense(10, tf.nn.softmax)
])

#definir algoritmo de treinamento, função de perda e métrica de treinamento
model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

#Treinar a rede
model.fit(x_train, y_train, epochs = 5)

#Avaliar a acurácia de rede no conjunto de teste
model.evaluate(x_test, y_test, verbose=2)