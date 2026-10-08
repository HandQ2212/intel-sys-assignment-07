import re

with open('report/main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_lstlisting = False

for i, line in enumerate(lines, 1):
    if r'\begin{lstlisting}' in line or r'\begin{verbatim}' in line:
        in_lstlisting = True
    if r'\end{lstlisting}' in line or r'\end{verbatim}' in line:
        in_lstlisting = False
        continue
        
    if in_lstlisting:
        continue
        
    # Ignore comments for % check - actually any % not escaped is a comment!
    # So we don't need to check %.
    
    # Check for &
    # We should ignore lines inside matrix, bmatrix, tabular, align, cases, eqnarray, etc.
    envs = ['bmatrix', 'matrix', 'tabular', 'align', 'cases', 'eqnarray', 'gather']
    if any(env in line for env in envs):
        continue
        
    # Check for unescaped #
    if re.search(r'(?<!\\)#', line):
        print(f"Line {i} unescaped #: {line.strip()}")

