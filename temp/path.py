"""Path"""

import os

print('=' * 40)
print("最後試到可行的方案")
'''
SAVE_PATH = os.path.realpath(os.path.dirname(__file__)) + "\\svg"
WM.render_to_file(os.path.join(SAVE_PATH, 'americas.svg'))
'''
print('=' * 40)





cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

print('=' * 40)
print("這是 Files in %r: %s" % (cwd, files))
print("當前工作路徑: " + os.getcwd())          #打印出当前工作路径
print('=' * 40)
print(os.path.dirname('d:\\library\\book.txt'))
print("這是去除路徑後結果: " + os.path.basename('d:\\library\\book.txt'))
print("這是取得目前工作目錄: " + os.getcwd())
print(os.path.join(os.getcwd(), "hello.txt"))

print('=' * 40)

A = os.getcwd()
B = os.path.dirname(__file__)
C = os.path.join(A, B)
D = os.path.join(os.getcwd(), os.path.dirname(__file__))
E = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
F = os.path.realpath(os.path.dirname(__file__)) + "\\temp_dir"

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)

print('=' * 40)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(__location__)
print('=' * 40)
