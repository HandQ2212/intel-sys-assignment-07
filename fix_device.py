import json

path = 'notebooks/CNN/CNN_PyTorch_CIFAR-10.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')" in source:
            new_source = source.replace(
                "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')",
                "device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')"
            )
            cell['source'] = new_source

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
