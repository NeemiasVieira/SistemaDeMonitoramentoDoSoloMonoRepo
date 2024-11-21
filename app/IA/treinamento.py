import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils.class_weight import compute_class_weight
import tensorflow as tf

def build_model(input_shape=(224, 224, 3)):
    """
    Constrói um modelo CNN com melhorias para maior precisão e generalização.
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.3),

        Conv2D(64, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.3),

        Conv2D(128, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.4),

        Flatten(),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),

        Dense(1, activation='sigmoid')  # Classificação binária
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', 'Precision', 'Recall'])
    return model

def train(data_dir, output_model_path):
    """
    Treina o modelo com os dados disponíveis.
    """
    datagen = ImageDataGenerator(validation_split=0.2, rescale=1./255)

    train_generator = datagen.flow_from_directory(
        data_dir, target_size=(224, 224), batch_size=32, class_mode='binary', subset='training')
    val_generator = datagen.flow_from_directory(
        data_dir, target_size=(224, 224), batch_size=32, class_mode='binary', subset='validation')

    # Cálculo de pesos de classe para balanceamento
    class_weights = compute_class_weight(
        class_weight='balanced',
        classes=np.unique(train_generator.classes),
        y=train_generator.classes
    )
    class_weights = dict(enumerate(class_weights))
    print(f"Pesos de classe: {class_weights}")

    model = build_model()
    model.fit(
        train_generator,
        validation_data=val_generator,
        epochs=20,  # Mais épocas para maior aprendizado
        class_weight=class_weights  # Balanceamento artificial
    )
    model.save(output_model_path)

if __name__ == "__main__":
    data_dir = "app/IA/data/processed"
    output_model_path = "app/IA/data/models/basil_model.keras"
    train(data_dir, output_model_path)
