import tensorflow as tf
import numpy as np
from tensorflow import keras

''' Problem
1 quarto -> 100k
2 quarto -> 150k
3 quarto -> 200K
    . . . 
'''

def main():
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], dtype=float)
    ys = np.array([50, 100.0, 150.0, 200.0, 250.00, 300.0, 350.0, 400.0], dtype=float)

    model.fit(xs, ys, epochs=1000)

    print(f'PRICE R${model.predict([8.0])/100}')

if __name__ == '__main__':
    main()
