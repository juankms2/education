# Simple CLI utility which allows merging multiple PDF files into a single merged_file.pdf
# At least two pdf file names are expected. They are merged in the order they are provided.
# Requires PyPDF2(https://pypi.org/project/PyPDF2/).
#
# Run with: python pdf_merger.py files/file1.pdf files/file3.pdf files/file2.pdf

import sys
import PyPDF2

args = sys.argv

if len(args) < 3:
    print('!! Invalid arguments. At least two pdf file names must be provided... ')
    exit()

pdf_files = args[1:]
print(f'>> Files to merge: {pdf_files}')

merger = PyPDF2.PdfMerger()
for pdf in pdf_files:
    try:
        merger.append(pdf)
    except FileNotFoundError:
        print(f'>> {pdf} not found! Skipping...')
    
if len(merger.pages) > 0:
    merger.write('merged_file.pdf')
    print('>> Done. "merged_file.pdf" was generated from the given files.')
else:
    print('>> Merged file not generated as there were no pages to print.')
