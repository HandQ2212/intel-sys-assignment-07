import json

def update_notebook(path, new_cells):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    final_cells = [nb['cells'][0]] + new_cells
    nb['cells'] = final_cells
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)

keras_cells = [
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import tensorflow as tf\n",
        "from tensorflow.keras.models import Sequential\n",
        "from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPooling2D, GlobalAveragePooling2D, Dense, Rescaling\n",
        "import os\n",
        "\n",
        "# Hyperparameters\n",
        "BATCH_SIZE = 64\n",
        "EPOCHS = 5\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Dataset Loading from ../../data/cifar10\n",
        "train_dir = '../../data/cifar10/train'\n",
        "test_dir = '../../data/cifar10/test'\n",
        "\n",
        "train_dataset = tf.keras.utils.image_dataset_from_directory(\n",
        "    train_dir,\n",
        "    labels='inferred',\n",
        "    label_mode='int',\n",
        "    batch_size=BATCH_SIZE,\n",
        "    image_size=(32, 32),\n",
        "    shuffle=True,\n",
        ")\n",
        "\n",
        "test_dataset = tf.keras.utils.image_dataset_from_directory(\n",
        "    test_dir,\n",
        "    labels='inferred',\n",
        "    label_mode='int',\n",
        "    batch_size=BATCH_SIZE,\n",
        "    image_size=(32, 32),\n",
        "    shuffle=False,\n",
        ")\n",
        "\n",
        "normalization_layer = Rescaling(1./255)\n",
        "train_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))\n",
        "test_dataset = test_dataset.map(lambda x, y: (normalization_layer(x), y))\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Model Definition (BasicCNN2D from assignment 05 translated to Keras)\n",
        "model = Sequential([\n",
        "    Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)),\n",
        "    BatchNormalization(),\n",
        "    Activation('relu'),\n",
        "    MaxPooling2D(pool_size=(2, 2)),\n",
        "    \n",
        "    Conv2D(64, (3, 3), padding='same'),\n",
        "    BatchNormalization(),\n",
        "    Activation('relu'),\n",
        "    MaxPooling2D(pool_size=(2, 2)),\n",
        "    \n",
        "    GlobalAveragePooling2D(),\n",
        "    Dense(10, activation='softmax')\n",
        "])\n",
        "\n",
        "model.compile(optimizer='adam',\n",
        "              loss='sparse_categorical_crossentropy',\n",
        "              metrics=['accuracy'])\n",
        "\n",
        "print('Keras CNN Model built')\n",
        "model.summary()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "history = model.fit(\n",
        "    train_dataset,\n",
        "    epochs=EPOCHS,\n",
        "    validation_data=test_dataset\n",
        ")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "loss, accuracy = model.evaluate(test_dataset)\n",
        "print(f\"Accuracy on test set: {accuracy * 100:.2f}%\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "os.makedirs('../../models', exist_ok=True)\n",
        "model_path = '../../models/CNN_Keras_CIFAR-10.h5'\n",
        "model.save(model_path)\n",
        "print('Saved Keras model to', model_path)\n"
      ]
    }
]

update_notebook('notebooks/CNN/CNN_Keras_CIFAR-10.ipynb', keras_cells)
