import re

with open('report/main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_lstlisting = False
in_math_display = False
in_math_inline = False

for i, line in enumerate(lines, 1):
    if r'\begin{lstlisting}' in line or r'\begin{verbatim}' in line:
        in_lstlisting = True
    if r'\end{lstlisting}' in line or r'\end{verbatim}' in line:
        in_lstlisting = False
        continue
        
    if in_lstlisting:
        continue
        
    # very naive check for unescaped _ outside $
    # we can just use regex to replace unescaped _ that are not in math mode.
    # Actually, a better approach is to print any line containing `_` that is not inside $...$ or $$...$$ or \[...\] or equation or align.
    
    # Let's just find lines with `_` and print them for manual inspection
    if '_' in line:
        # Ignore comments
        if line.lstrip().startswith('%'):
            continue
        # Ignore lines with math environments that typically contain _
        math_envs = ['equation', 'align', 'eqnarray', 'gather', r'\[', r'\]']
        if any(env in line for env in math_envs):
            continue
        if r'\url{' in line or r'\includegraphics' in line or r'\IfFileExists' in line or r'\label{' in line or r'\ref{' in line:
            continue
            
        # check if the _ is inside inline math $...$
        # Count number of $ before the _
        # A simpler way: split by $, if the _ is in an odd index, it's in math mode.
        parts = line.split('$')
        outside_math = False
        for j, part in enumerate(parts):
            if j % 2 == 0: # outside math mode
                if re.search(r'(?<!\\)_', part):
                    outside_math = True
                    break
        
        if outside_math:
            print(f"{i}: {line.strip()}")

