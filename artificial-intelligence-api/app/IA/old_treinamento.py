import os
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

dataset_dir = os.path.join(os.getcwd(), 'basil_images')

dataset_train_dir = os.path.join(dataset_dir, 'train')
dataset_train_saudavel_len = len(os.listdir(os.path.join(dataset_train_dir, 'saudavel')))
dataset_train_doente_len = len(os.listdir(os.path.join(dataset_train_dir, 'nao_saudavel')))

dataset_validation_dir = os.path.join(dataset_dir, 'valid')
dataset_validation_saudavel_len = len(os.listdir(os.path.join(dataset_validation_dir, 'saudavel')))
dataset_validation_doente_len = len(os.listdir(os.path.join(dataset_validation_dir, 'nao_saudavel')))

print('Train saudavel:%s' % dataset_train_saudavel_len)
print('Train doente:%s' % dataset_train_doente_len)
print('validation saudavel:%s' % dataset_validation_saudavel_len)
print('validation doente:%s' % dataset_validation_doente_len)

image_width = 160
image_height = 160
image_color_channel = 3
image_color_channel_size = 255
image_size = (image_width, image_height)
image_shape = image_size + (image_color_channel,)

batch_size = 32 #quantidade de imagens que serao trasidas do dataset por vez
epochs = 20 #numero de fezes que passara pelo dataset inteiro
learning_rate = 0.0001 #taxa de aprendizagem

class_names = ["notHealth", "health"]

dataset_train = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_train_dir,
    image_size = image_size,
    batch_size = batch_size,
    shuffle = True
)

dataset_validation = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_validation_dir,
    image_size = image_size,
    batch_size = batch_size,
    shuffle = True
)

dataset_validation_cardinality = tf.data.experimental.cardinality(dataset_validation)
dataset_validation_batches = dataset_validation_cardinality // 5

dataset_test = dataset_validation.take(dataset_validation_batches)
dataset_validation = dataset_validation.skip(dataset_validation_batches)

print('Validation Dataset Cardinality: %d' % tf.data.experimental.cardinality(dataset_validation))
print('Test Dataset Cardinality: %d' % tf.data.experimental.cardinality(dataset_test))

def plot_dataset(dataset):
    plt.gcf().clear()
    plt.figure(figsize=(15,15))

    for features, labels in dataset.take(1):
        for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.axis('off')

            plt.imshow(features[i].numpy().astype('uint8'))
            plt.title(class_names[labels[i]])

plot_dataset(dataset_train)
plot_dataset(dataset_validation)
plot_dataset(dataset_test)
model = Sequential([
    Rescaling(
        1. / image_color_channel_size,
        input_shape = image_shape
    ),
    Conv2D(16, 3, padding = 'same', activation = 'relu'),
    MaxPooling2D(),
    Conv2D(32, 3, padding = 'same', activation = 'relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding = 'same', activation = 'relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(128, activation = 'relu'),
    Dense(1, activation = 'sigmoid')
])

model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate = learning_rate),
    loss = tf.keras.losses.BinaryCrossentropy(),
    metrics = ['accuracy']
)

model.summary()

history = model.fit(
    dataset_train,
    validation_data = dataset_validation,
    epochs = epochs
)

def plot_dataset_predictions(dataset):
    features, labels = dataset.as_numpy_iterator().next()

    predictions = model.predict_on_batch(features).flatten()
    predictions = tf.where(predictions < 0.5, 0, 1)

    print('Label:       %s' % labels)
    print('predictions: %s' % predictions.numpy())

    plt.gcf().clear()
    plt.figure(figsize = (15,15))

    for i in range(9):
            plt.subplot(3, 3, i + 1)
            plt.axis('off')

            plt.imshow(features[i].astype('uint8'))
            plt.title(class_names[predictions[i]])

plot_dataset_predictions(dataset_test)
model.save('./model2.keras')
