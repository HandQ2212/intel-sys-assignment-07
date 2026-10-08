import re

with open('report/main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_verb = False
in_math_env = False

for i, line in enumerate(lines, 1):
    if r'\begin{lstlisting}' in line or r'\begin{verbatim}' in line:
        in_verb = True
    if r'\end{lstlisting}' in line or r'\end{verbatim}' in line:
        in_verb = False
        continue
        
    if any(env in line for env in [r'\begin{align}', r'\begin{align*}', r'\begin{tabular}', r'\begin{cases}', r'\begin{bmatrix}', r'\begin{eqnarray}']):
        in_math_env = True
    if any(env in line for env in [r'\end{align}', r'\end{align*}', r'\end{tabular}', r'\end{cases}', r'\end{bmatrix}', r'\end{eqnarray}']):
        in_math_env = False
        continue
        
    if in_verb or in_math_env:
        continue
        
    if re.search(r'(?<!\\)&', line) and not line.lstrip().startswith('%'):
        print(f"Line {i} unescaped &: {line.strip()}")

