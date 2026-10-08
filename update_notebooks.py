import json

def update_notebook(path, new_cells):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    # Keep the first markdown cell
    final_cells = [nb['cells'][0]] + new_cells
    nb['cells'] = final_cells
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)

# ================== PyTorch ==================
pytorch_cells = [
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "import torch\n",
        "import torch.nn as nn\n",
        "import torch.optim as optim\n",
        "from torchvision import datasets, transforms\n",
        "from torch.utils.data import DataLoader\n",
        "import os\n",
        "\n",
        "# Hyperparameters\n",
        "BATCH_SIZE = 64\n",
        "EPOCHS = 5\n",
        "LEARNING_RATE = 1e-3\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "# Dataset Loading from ../../data/cifar10\n",
        "train_transform = transforms.Compose([\n",
        "    transforms.Resize((32, 32)),\n",
        "    transforms.RandomHorizontalFlip(),\n",
        "    transforms.RandomCrop(32, padding=4),\n",
        "    transforms.ToTensor(),\n",
        "    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))\n",
        "])\n",
        "test_transform = transforms.Compose([\n",
        "    transforms.Resize((32, 32)),\n",
        "    transforms.ToTensor(),\n",
        "    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))\n",
        "])\n",
        "\n",
        "train_dir = '../../data/cifar10/train'\n",
        "test_dir = '../../data/cifar10/test'\n",
        "\n",
        "train_dataset = datasets.ImageFolder(train_dir, transform=train_transform)\n",
        "test_dataset = datasets.ImageFolder(test_dir, transform=test_transform)\n",
        "\n",
        "train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)\n",
        "test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)\n",
        "\n",
        "print(f\"Loaded {len(train_dataset)} training images and {len(test_dataset)} testing images.\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "class BasicCNN2D(nn.Module):\n",
        "    def __init__(self, in_channels=3, num_classes=10):\n",
        "        super().__init__()\n",
        "        self.features = nn.Sequential(\n",
        "            nn.Conv2d(in_channels, 32, kernel_size=3, padding=1),\n",
        "            nn.BatchNorm2d(32),\n",
        "            nn.ReLU(inplace=True),\n",
        "            nn.MaxPool2d(2),\n",
        "            nn.Conv2d(32, 64, kernel_size=3, padding=1),\n",
        "            nn.BatchNorm2d(64),\n",
        "            nn.ReLU(inplace=True),\n",
        "            nn.MaxPool2d(2),\n",
        "        )\n",
        "        self.classifier = nn.Sequential(\n",
        "            nn.AdaptiveAvgPool2d(1),\n",
        "            nn.Flatten(),\n",
        "            nn.Linear(64, num_classes),\n",
        "        )\n",
        "\n",
        "    def forward(self, x):\n",
        "        return self.classifier(self.features(x))\n",
        "\n",
        "model = BasicCNN2D()\n",
        "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n",
        "model.to(device)\n",
        "print('PyTorch CNN Model initialized')\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "criterion = nn.CrossEntropyLoss()\n",
        "optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)\n",
        "\n",
        "for epoch in range(EPOCHS):\n",
        "    model.train()\n",
        "    running_loss = 0.0\n",
        "    for inputs, labels in train_loader:\n",
        "        inputs, labels = inputs.to(device), labels.to(device)\n",
        "        \n",
        "        optimizer.zero_grad()\n",
        "        outputs = model(inputs)\n",
        "        loss = criterion(outputs, labels)\n",
        "        loss.backward()\n",
        "        optimizer.step()\n",
        "        \n",
        "        running_loss += loss.item() * inputs.size(0)\n",
        "    \n",
        "    epoch_loss = running_loss / len(train_dataset)\n",
        "    print(f\"Epoch {epoch+1}/{EPOCHS}, Loss: {epoch_loss:.4f}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "model.eval()\n",
        "correct = 0\n",
        "total = 0\n",
        "with torch.no_grad():\n",
        "    for inputs, labels in test_loader:\n",
        "        inputs, labels = inputs.to(device), labels.to(device)\n",
        "        outputs = model(inputs)\n",
        "        _, predicted = torch.max(outputs.data, 1)\n",
        "        total += labels.size(0)\n",
        "        correct += (predicted == labels).sum().item()\n",
        "\n",
        "print(f\"Accuracy on test set: {100 * correct / total:.2f}%\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "os.makedirs('../../models', exist_ok=True)\n",
        "model_path = '../../models/CNN_PyTorch_CIFAR-10.pth'\n",
        "torch.save(model.state_dict(), model_path)\n",
        "print('Saved PyTorch model to', model_path)\n"
      ]
    }
]

update_notebook('notebooks/CNN/CNN_PyTorch_CIFAR-10.ipynb', pytorch_cells)
