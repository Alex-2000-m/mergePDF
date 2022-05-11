import os
from PyPDF2 import PdfFileMerger

target_path = r'pdf'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf,import_bookmarks=False)     # 合并pdf文件

file_merger.write(r"merge.pdf")

