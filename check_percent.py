import re

with open('report/main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    # check if % is in the line and not at the beginning and not preceded by \
    # We ignore standard comments that start the line
    stripped = line.lstrip()
    if not stripped.startswith('%') and '%' in stripped:
        if re.search(r'(?<!\\)%', line):
            print(f"Line {i} inline comment: {line.strip()}")

