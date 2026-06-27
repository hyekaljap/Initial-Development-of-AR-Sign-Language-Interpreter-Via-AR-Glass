import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# ── 1. Settings ──────────────────────────────────────────────
base = r"D:\User\Documents\#UTM\SEMESTER 6\PSM1\InitialMSL\MSL"
classes = ['A', 'B', 'C', 'other']
IMG_SIZE = 128

# ── 2. Load images ───────────────────────────────────────────
data = []
labels = []

for label_id, class_name in enumerate(classes):
    folder = os.path.join(base, class_name)
    if not os.path.exists(folder):
        print(f"WARNING: folder not found: {folder}")
        continue
    count = 0
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img = cv2.imread(os.path.join(folder, filename))
            if img is None:
                continue
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            data.append(img)
            labels.append(label_id)
            count += 1
    print(f"{class_name}: {count} images (label {label_id})")

data = np.array(data) / 255.0
labels = np.array(labels)
print(f"Total: {len(data)} images")

# ── 3. Split ─────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42, stratify=labels
)

print(f"Train: {len(X_train)} | Test: {len(X_test)}")

# ── 4. Build CNN ─────────────────────────────────────────────
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(256, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(classes), activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ── 5. Train ─────────────────────────────────────────────────
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# ── 6. Save ──────────────────────────────────────────────────
save_path = os.path.join(base, "msl_model.h5")
model.save(save_path)
print(f"Model saved to: {save_path}")

# ── 7. Plot ──────────────────────────────────────────────────
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Val')
plt.title('Accuracy')
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Val')
plt.title('Loss')
plt.legend()

plt.savefig(os.path.join(base, 'training_result.png'))
plt.show()
print("Done!")