# Remove the extension from a Filename in Python 

import os

file_path = '/home/bobbyhadz/Desktop/my-file.txt'

result = os.path.splitext(file_path)[0]

# 👇️ '/home/bobbyhadz/Desktop/my-file'
print(result)

# 👇️ '/home/bobbyhadz/Desktop/my-file.docx'
print(result + '.docx')