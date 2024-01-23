import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Generate dummy dataset structure for demonstration
base_dir = 'dummy_dataset'
os.makedirs(base_dir, exist_ok=True)

for class_name in ['cats', 'dogs']:
    class_dir = os.path.join(base_dir, class_name)
    os.makedirs(class_dir, exist_ok=True)
    for i in range(100):
        # Create dummy images (you may use real images)
        img_path = os.path.join(class_dir, f'{class_name}_{i}.jpg')
        # Save the dummy image (replace this with your image loading logic)
        plt.imsave(img_path, np.random.rand(64, 64, 3))

# Define a more advanced convolutional neural network (CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.25),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(2, activation='softmax')  # Assuming 2 classes (cats and dogs)
])

# Compile the model with Adam optimizer and categorical crossentropy loss
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Load and preprocess data with advanced data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Replace 'dummy_dataset' with the actual path to your dataset
train_generator = train_datagen.flow_from_directory(
    'dummy_dataset',
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical'
)

# Train the model with increased epochs and steps_per_epoch
model.fit(train_generator, epochs=20, steps_per_epoch=len(train_generator))
