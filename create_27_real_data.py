import json
import os

def get_markdown_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": [source + "\n"]}

def get_code_cell(source):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in source.split('\n')]}

def save_nb(cells, filepath):
    nb = {"cells": cells, "metadata": {}, "nbformat": 4, "nbformat_minor": 4}
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)

def get_ml_data_code(name):
    if name == "Diabetes":
        return """import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../../data/diabetes.csv')
X = df.drop('Outcome', axis=1).values
y = df['Outcome'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(f"Loaded Diabetes dataset: X_train {X_train.shape}")"""
    elif name == "Housing":
        return """import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('../../data/vietnam_housing_dataset.csv').dropna()
X = df[['Diện tích', 'Số phòng ngủ', 'Số phòng vệ sinh']].values
y = df['Giá'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(f"Loaded Housing dataset: X_train {X_train.shape}")"""
    elif name == "Ecommerce":
        return """import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('../../data/Womens Clothing E-Commerce Reviews.csv').dropna(subset=['Review Text', 'Recommended IND'])
X_text = df['Review Text'].values
y = df['Recommended IND'].values
vectorizer = TfidfVectorizer(max_features=100)
X = vectorizer.fit_transform(X_text).toarray()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Loaded Ecommerce dataset: X_train {X_train.shape}")"""

def get_cnn_data_code(name, fw):
    if name == "CIFAR-10":
        if fw == "Keras":
            return """import numpy as np
from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0
print(f"Loaded CIFAR-10 Keras: X_train {X_train.shape}")"""
        elif fw == "PyTorch":
            return """import torch
import torchvision
import torchvision.transforms as transforms
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
print("Loaded CIFAR-10 PyTorch")"""
        else:
            return """import numpy as np
from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
X_train = X_train.astype('float32') / 255.0
print(f"Loaded CIFAR-10 Numpy: X_train {X_train.shape}")"""
    elif name == "MNIST":
        if fw == "Keras":
            return """import numpy as np
from tensorflow.keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
print(f"Loaded MNIST Keras: X_train {X_train.shape}")"""
        elif fw == "PyTorch":
            return """import torch
import torchvision
import torchvision.transforms as transforms
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
print("Loaded MNIST PyTorch")"""
        else:
            return """import numpy as np
from tensorflow.keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
print(f"Loaded MNIST Numpy: X_train {X_train.shape}")"""
    elif name == "Diabetes_1D":
        return """import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('../../data/diabetes.csv')
X = df.drop('Outcome', axis=1).values
y = df['Outcome'].values
X = StandardScaler().fit_transform(X)
X_train = X.reshape(X.shape[0], X.shape[1], 1)
print(f"Loaded Diabetes 1D dataset: X_train {X_train.shape}")"""

def get_rnn_data_code(name):
    filename = "gold_price.csv" if name == "Gold_Price" else ("AMZN.csv" if name == "AMZN_Stock" else "gold_silver_data/silver_price.csv")
    col_name = "Price" if name == "Gold_Price" or name == "Silver_Price" else "Close"
    return f"""import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('../../data/{filename}')
# Drop NA just in case
df = df.dropna()
data = df['{col_name}' if '{col_name}' in df.columns else df.columns[1]].values.reshape(-1, 1)

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

def create_sequences(data, seq_length):
    xs, ys = [], []
    for i in range(len(data)-seq_length):
        xs.append(data[i:i+seq_length])
        ys.append(data[i+seq_length])
    return np.array(xs), np.array(ys)

X_train, y_train = create_sequences(data_scaled[:int(len(data)*0.8)], 30)
X_test, y_test = create_sequences(data_scaled[int(len(data)*0.8):], 30)
print(f"Loaded {name} dataset: X_train {{X_train.shape}}")"""

base_dir = 'd:/DaiHoc/Nam4/LTHTTM/assignment_07/notebooks'

datasets_ml = ["Diabetes", "Housing", "Ecommerce"]
datasets_cnn = ["CIFAR-10", "MNIST", "Diabetes_1D"]
datasets_rnn = ["Gold_Price", "AMZN_Stock", "Silver_Price"]

for fw in ["NumPy", "Keras", "PyTorch"]:
    # ML
    for name in datasets_ml:
        cells = [
            get_markdown_cell(f"# Chương 2: ML Cơ bản - Framework: {fw} - Dataset: {name}"),
            get_code_cell(get_ml_data_code(name))
        ]
        if fw == "NumPy":
            cells.append(get_code_cell(f"class ML_{name}_{fw}:\n    def __init__(self, input_dim):\n        self.W = np.random.randn(input_dim, 1)\n    def forward(self, X):\n        return X.dot(self.W)\nmodel = ML_{name}_{fw}(X_train.shape[1])\nprint('Model initialized')"))
        elif fw == "Keras":
            cells.append(get_code_cell(f"from tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Dense\nmodel = Sequential([Dense(16, activation='relu', input_shape=(X_train.shape[1],)), Dense(1)])\nmodel.compile(optimizer='adam', loss='mse')\nmodel.fit(X_train, y_train, epochs=2, batch_size=32)\nprint('Keras Model trained')"))
        elif fw == "PyTorch":
            cells.append(get_code_cell(f"import torch\nimport torch.nn as nn\nclass ML_Torch(nn.Module):\n    def __init__(self, in_features):\n        super().__init__()\n        self.net = nn.Sequential(nn.Linear(in_features, 16), nn.ReLU(), nn.Linear(16, 1))\n    def forward(self, x):\n        return self.net(x)\nmodel = ML_Torch(X_train.shape[1])\nprint('PyTorch Model initialized')"))
        save_nb(cells, os.path.join(base_dir, 'ML', f'ML_{fw}_{name}.ipynb'))

    # CNN
    for name in datasets_cnn:
        cells = [
            get_markdown_cell(f"# Chương 3: Mạng Tích chập (CNN) - Framework: {fw} - Dataset: {name}"),
            get_code_cell(get_cnn_data_code(name, fw))
        ]
        if fw == "NumPy":
            cells.append(get_code_cell(f"class CNN_{name}_{fw}:\n    def __init__(self):\n        pass\n    def forward(self, x):\n        pass\nmodel = CNN_{name}_{fw}()\nprint('NumPy CNN Model initialized')"))
        elif fw == "Keras":
            if name == "Diabetes_1D":
                cells.append(get_code_cell("from tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Conv1D, Flatten, Dense\nmodel = Sequential([Conv1D(16, 3, activation='relu', input_shape=(21,1)), Flatten(), Dense(1)])\nmodel.compile(optimizer='adam', loss='binary_crossentropy')\nprint('Keras CNN 1D Model built')"))
            else:
                input_shape = "(32, 32, 3)" if name=="CIFAR-10" else "(28, 28, 1)"
                cells.append(get_code_cell(f"from tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import Conv2D, Flatten, Dense\nmodel = Sequential([Conv2D(16, (3,3), input_shape={input_shape}), Flatten(), Dense(10)])\nmodel.compile(optimizer='adam', loss='sparse_categorical_crossentropy')\nprint('Keras CNN Model built')"))
        elif fw == "PyTorch":
            cells.append(get_code_cell(f"import torch.nn as nn\nclass CNN_Torch(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.conv = nn.Conv2d(3 if '{name}'=='CIFAR-10' else 1, 16, 3)\nmodel = CNN_Torch()\nprint('PyTorch CNN Model initialized')"))
        save_nb(cells, os.path.join(base_dir, 'CNN', f'CNN_{fw}_{name}.ipynb'))

    # RNN
    for name in datasets_rnn:
        cells = [
            get_markdown_cell(f"# Chương 4: Mạng Hồi quy (RNN) - Framework: {fw} - Dataset: {name}"),
            get_code_cell(get_rnn_data_code(name))
        ]
        if fw == "NumPy":
            cells.append(get_code_cell(f"class RNN_{name}_{fw}:\n    def __init__(self):\n        self.W = np.random.randn(16, 16)\nmodel = RNN_{name}_{fw}()\nprint('NumPy RNN Model initialized')"))
        elif fw == "Keras":
            cells.append(get_code_cell(f"from tensorflow.keras.models import Sequential\nfrom tensorflow.keras.layers import SimpleRNN, Dense\nmodel = Sequential([SimpleRNN(16, input_shape=(30, 1)), Dense(1)])\nmodel.compile(optimizer='adam', loss='mse')\nmodel.fit(X_train, y_train, epochs=2, batch_size=32)\nprint('Keras RNN Model trained')"))
        elif fw == "PyTorch":
            cells.append(get_code_cell(f"import torch.nn as nn\nclass RNN_Torch(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.rnn = nn.RNN(1, 16, batch_first=True)\nmodel = RNN_Torch()\nprint('PyTorch RNN Model initialized')"))
        save_nb(cells, os.path.join(base_dir, 'RNN', f'RNN_{fw}_{name}.ipynb'))
