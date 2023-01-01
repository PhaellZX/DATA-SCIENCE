import tensorflow as tf
import keras.datasets.mnist as mnist

class MyCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.99:
            print("\nReached 99% accuracy so cancelling training!")
            self.model.stop_training = True

def main():

    # You code should start here
    hands_mninst = tf.keras.datasets.mnist
    # You code should start here

    (training_images, training_labels), (test_images, test_labels) = hands_mninst.load_data()

    # You code should start here
    train_images = training_images / 255.0
    test_images = test_images / 255.0
    # You code should start here


    model = tf.keras.models.Sequential([

        # You code should start here
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),  # hidden layer
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        # You code should start here

    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    callbacks = MyCallback()

    #model fitting
    history = model.fit(
        # You code should start here
        train_images,
        training_labels,
        epochs=5,
        callbacks=[callbacks]
        # You code should start here
    )
    print(history.epoch, history.history['accuracy'][-1])

if __name__ == '__main__':
    main()