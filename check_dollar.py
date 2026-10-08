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
        
    # count $
    # Ignore lines with $$ because they are complete blocks, but wait, $$ can be on separate lines.
    # A simple check: if line contains exactly one $, or an odd number of $.
    
    # We should strip comments first
    idx = line.find('%')
    if idx != -1 and (idx == 0 or line[idx-1] != '\\'):
        line = line[:idx]
        
    # find unescaped $
    dollars = re.findall(r'(?<!\\)\$', line)
    if len(dollars) % 2 != 0:
        # It's possible it's a $$ split across lines, but let's check
        print(f"Line {i} odd dollars ({len(dollars)}): {line.strip()}")

