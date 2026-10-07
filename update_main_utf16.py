import io

with io.open("report/main.tex.tmp", "r", encoding="utf-16-le") as f:
    content = f.read()

content = content.replace("BÁO CÁO KỸ THUẬT ASSIGNMENT 06", "TIỂU LUẬN CUỐI KỲ")
content = content.replace("ASSIGNMENT 06 -- LTHTTM", "TIỂU LUẬN CUỐI KỲ -- LTHTTM")
content = content.replace("MỤC LỤC BÁO CÁO KỸ THUẬT ASSIGNMENT 06", "MỤC LỤC TIỂU LUẬN")
# Remove from \section*{TÓM TẮT BÁO CÁO (ABSTRACT)} onwards and replace
abstract_idx = content.find("\\section*{TÓM TẮT BÁO CÁO")
if abstract_idx != -1:
    content = content[:abstract_idx]

tail = r"""\section*{TÓM TẮT BÁO CÁO (ABSTRACT)}
\addcontentsline{toc}{section}{TÓM TẮT BÁO CÁO (ABSTRACT)}

Tiểu luận môn học Lập trình hệ thống thông minh trình bày tổng quan về Trí tuệ nhân tạo, từ lịch sử phát triển cho đến các kỹ thuật Học máy (Machine Learning) cơ bản, Mạng nơ-ron Tích chập (CNN) và Mạng nơ-ron Hồi quy (RNN). Báo cáo thực hiện khảo sát các tập dữ liệu, xây dựng mô hình từ đầu (from scratch) cho đến sử dụng các framework hiện đại như Keras và PyTorch, đồng thời so sánh đánh giá hiệu năng và triển khai ứng dụng thực tế.

\newpage

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
content += tail

with io.open("report/main.tex", "w", encoding="utf-8") as f:
    f.write(content)
