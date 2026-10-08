import re

main_file = "report/main.tex"

with open(main_file, "r", encoding="utf-8") as f:
    main_content = f.read()

def replace_input(match):
    chapter_file = match.group(1)
    if not chapter_file.endswith('.tex'):
        chapter_file += '.tex'
    # The path in \input{} is usually relative to report/
    full_path = f"report/{chapter_file}"
    try:
        with open(full_path, "r", encoding="utf-8") as cf:
            content = cf.read()
            return f"% --- BẮT ĐẦU {chapter_file} ---\n{content}\n% --- KẾT THÚC {chapter_file} ---\n"
    except Exception as e:
        print(f"Lỗi đọc file {full_path}: {e}")
        return match.group(0)

# Tìm các pattern dạng \input{chapters/00_intro} hoặc \input{chapters/00_intro.tex}
merged_content = re.sub(r'\\input\{([^}]+)\}', replace_input, main_content)

with open(main_file, "w", encoding="utf-8") as f:
    f.write(merged_content)

print("Đã gộp tất cả các chapter vào main.tex")
