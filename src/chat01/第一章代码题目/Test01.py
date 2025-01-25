#要求：使用print函数将"人生苦短，我用python"输出到文本文件text.txt中
fp=open('note.txt', 'w')#打开文件 W-->write
print("人生苦短，我用python",file=fp)
fp.close()