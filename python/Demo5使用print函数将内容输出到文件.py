fp=open('note.txt','w') #建立的文件名叫做note.txt 其中w=write是打开文件的
print('北京欢迎你',file=fp) #将北京欢迎你输出1或者到note.txt当中
fp.close() #关闭文件