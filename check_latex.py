import re

def check_tex(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove environments that allow math or verbatim
    envs_to_remove = ['lstlisting', 'verbatim', 'equation', 'equation*', 'align', 'align*', 'eqnarray', 'eqnarray*', 'gather', 'gather*']
    
    for env in envs_to_remove:
        pattern = r'\\begin\{' + env + r'\}.*?\\end\{' + env + r'\}'
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Remove math mode block $$...$$ and \[ ... \]
    content = re.sub(r'\$\$.*?\$\$', '', content, flags=re.DOTALL)
    content = re.sub(r'\\\[.*?\\\]', '', content, flags=re.DOTALL)
    
    # Remove inline math $...$
    content = re.sub(r'\$.*?\$', '', content)
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        # find unescaped _ outside math/verb modes
        # Also let's check for _ not preceded by \
        if re.search(r'(?<!\\)_', line):
            # Ignore comment lines
            if line.strip().startswith('%'):
                continue
            # Ignore URL/href which might have _ but we should probably escape them unless they are in \url{}
            # But let's just print
            print(f"Line {i}: unescaped underscore: {line.strip()}")
            
check_tex('report/main.tex')
