import re

with open("report/main.tex", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the title part
content = re.sub(r'BÁO CÁO KỸ THUẬT ASSIGNMENT 06', r'TIỂU LUẬN CUỐI KỲ', content)
content = re.sub(r'ASSIGNMENT 06 -- LTHTTM', r'TIỂU LUẬN CUỐI KỲ -- LTHTTM', content)
content = re.sub(r'MỤC LỤC BÁO CÁO KỸ THUẬT ASSIGNMENT 06', r'MỤC LỤC TIỂU LUẬN', content)
content = re.sub(r'Báo cáo Kỹ thuật Assignment 06 trình bày.*', r'Tiểu luận môn học Lập trình hệ thống thông minh trình bày tổng quan về Trí tuệ nhân tạo, từ lịch sử phát triển cho đến các kỹ thuật Học máy (Machine Learning) cơ bản, Mạng nơ-ron Tích chập (CNN) và Mạng nơ-ron Hồi quy (RNN). Báo cáo thực hiện khảo sát các tập dữ liệu, xây dựng mô hình từ đầu (from scratch bằng NumPy) cho đến sử dụng các framework hiện đại như Keras và PyTorch, đồng thời so sánh đánh giá hiệu năng và triển khai ứng dụng thực tế.', content, flags=re.DOTALL)

# Truncate after abstract and add chapter includes
abstract_end = content.find(r'\newpage', content.find('TÓM TẮT BÁO CÁO (ABSTRACT)'))
if abstract_end != -1:
    content = content[:abstract_end] + r"""\newpage

\include{chapters/00_intro}
\include{chapters/01_history}
\include{chapters/02_ml}
\include{chapters/03_cnn}
\include{chapters/04_rnn}

\newpage
\section*{Tài liệu tham khảo}
\addcontentsline{toc}{section}{Tài liệu tham khảo}
\begin{enumerate}[label={[\arabic*]}]
    \item Goodfellow, I., Bengio, Y., \& Courville, A. (2016). \textit{Deep Learning}. MIT Press.
    \item Russell, S., \& Norvig, P. (2020). \textit{Artificial Intelligence: A Modern Approach}. Pearson.
    \item Các tài liệu thực hành và bài giảng môn Lập trình hệ thống thông minh.
\end{enumerate}

\end{document}
"""

with open("report/main.tex", "w", encoding="utf-8") as f:
    f.write(content)
