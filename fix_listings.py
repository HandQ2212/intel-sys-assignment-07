import re

def remove_accents(input_str):
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s

with open('report/main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find \begin{lstlisting} ... \end{lstlisting}
pattern = re.compile(r'\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}', re.DOTALL)

def replacer(match):
    code_block = match.group(1)
    # only strip accents from the code content, not from the options if they contain captions
    # wait, match.group(1) includes the optional [caption=...] part if it's on the same line?
    # No, the regex \\begin\{lstlisting\}(.*?) will capture from right after the closing brace.
    # Ah, if there are optional arguments like \begin{lstlisting}[language=Python],
    # the capture group will start with [language=Python].
    return "\\begin{lstlisting}" + remove_accents(code_block) + "\\end{lstlisting}"

new_content = pattern.sub(replacer, content)

with open('report/main.tex', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Accents stripped from all lstlisting environments.")
