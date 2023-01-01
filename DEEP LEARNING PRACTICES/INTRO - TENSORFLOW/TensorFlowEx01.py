import keras
import tensorflow as tf
import numpy as np

'''
Problem:
y = 2 * x - 1
'''


def main():
    #Cria o modelo sequencial com 1 camada (1 neurônio) e 1 dado de entrada
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    #Inicializa os dados de entrada como dois arrays
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

    #define o modelo (exemplos e épocas para treinamento)
    model.fit(xs, ys, epochs=500)

    #faz a predição do modelo para valor de entrada 10
    print(model.predict([10.0]))


if __name__ == '__main__':
    main()

