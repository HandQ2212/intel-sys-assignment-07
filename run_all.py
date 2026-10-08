import os
import subprocess
import glob

notebooks = glob.glob('notebooks/**/*.ipynb', recursive=True)

for nb in notebooks:
    model_name = os.path.basename(nb).replace('.ipynb', '')
    
    # Check if model exists
    # Model extensions can be .pkl, .h5, .pt, .pth
    exists = False
    for ext in ['.pkl', '.h5', '.pt', '.pth']:
        if os.path.exists(f'models/{model_name}{ext}'):
            exists = True
            break
            
    if not exists:
        print(f"Executing missing model: {nb}...")
        try:
            # We use a timeout to prevent hanging, or let it run
            res = subprocess.run([
                'python3', '-m', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', nb
            ], capture_output=True, text=True, timeout=120)
            if res.returncode != 0:
                print(f"FAILED {nb}:\n{res.stderr[-500:]}")
            else:
                print(f"SUCCESS {nb}")
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT {nb}")
    else:
        print(f"Skipping {nb}, model already exists.")
