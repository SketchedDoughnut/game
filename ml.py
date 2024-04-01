def model1():
    import tensorflow as tf
    print('----------------------------')
    print('Tensorflow version:', tf.__version__)
    print('----------------------------')

    # create mnist dataset?
    mnist = tf.keras.datasets.mnist
    # get x and y training values, x and y testing values in tuples(?) by loading data from mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # divide by 255 (the color range) to get a binary 1/0?
    x_train, x_test = x_train / 255.0, x_test / 255.0


    model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
    ])


    predictions = model(x_train[:1]).numpy()
    predictions


    tf.nn.softmax(predictions).numpy()


    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


    loss_fn(y_train[:1], predictions).numpy()


    model.compile(optimizer='adam',
                loss=loss_fn,
                metrics=['accuracy'])


    model.fit(x_train, y_train, epochs=5)


    model.evaluate(x_test,  y_test, verbose=2)


    probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
    ])


    probability_model(x_test[:5])

def model2():
    # TensorFlow and tf.keras
    import tensorflow as tf

    # Helper libraries
    import numpy as np
    import matplotlib.pyplot as plt

    print('----------------------------')
    print('Tensorflow version:', tf.__version__)
    print('----------------------------')

    f_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = f_mnist.load_data()

    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    print('train images shape:', train_images.shape)
    print('train labels length:', len(train_labels))
    print('train labels:', train_labels)
    print('test images shape:', test_images.shape)
    print('test labels length:', len(test_labels))
    print('test labels:', test_labels)
    print('----------------------------')

    # plt.figure()
    # plt.imshow(train_images[0])
    # plt.colorbar()
    # plt.grid(False)
    # plt.show()

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy']
    )

    model.fit(train_images, train_labels, epochs=10)


    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    print('\nTest accuracy:', test_acc)
    print('Test loss:', test_loss, '\n')

    probability_model = tf.keras.Sequential(
        [
            model, 
            tf.keras.layers.Softmax()
        ]
    )

    # predictions = probability_model.predict(test_images)
    # they match, 9 -> 9
    # print(np.argmax(predictions[0]))
    # print(test_labels[0])

    # actual run
    print('----------------------------')
    print('----------------------------')
    for i in range(len(test_images)):
        img = test_images[i]
        img = (np.expand_dims(img,0))
    predictions_single = probability_model.predict(img)
    #print(np.argmax(predictions_single[0]))


# https://www.tensorflow.org/tutorials/quickstart/beginner
model1()  

# https://www.tensorflow.org/tutorials/keras/classification
model2()

''' 
Other links
    - https://www.tensorflow.org/
    - https://www.tensorflow.org/tutorials
    - https://hackajob.com/talent/blog/top-10-open-source-python-libraries-and-frameworks-for-machine-learning-in-2022
'''
