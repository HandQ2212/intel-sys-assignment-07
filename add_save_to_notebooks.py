import os
import json

base_dir = 'd:/DaiHoc/Nam4/LTHTTM/assignment_07/notebooks'
for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.ipynb'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                nb = json.load(file)
            
            # Check what framework it is based on filename
            model_name = f.replace('.ipynb', '')
            save_code = f"""import os
os.makedirs('../../models', exist_ok=True)
model_path = '../../models/{model_name}'
"""
            if 'NumPy' in f:
                save_code += f"""import pickle
with open(model_path + '.pkl', 'wb') as f:
    pickle.dump(model, f)
print('Saved NumPy model to', model_path + '.pkl')"""
            elif 'Keras' in f:
                save_code += f"""model.save(model_path + '.h5')
print('Saved Keras model to', model_path + '.h5')"""
            elif 'PyTorch' in f:
                save_code += f"""import torch
torch.save(model.state_dict(), model_path + '.pt')
print('Saved PyTorch model to', model_path + '.pt')"""
            
            new_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + '\n' for line in save_code.split('\n')]
            }
            nb['cells'].append(new_cell)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(nb, file, indent=2, ensure_ascii=False)
