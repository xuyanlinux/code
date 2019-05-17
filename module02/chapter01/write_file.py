
# f = open(file='write.txt',mode='w',encoding='gbk')
# f.write('世界，你好')
# f.close()

f = open(file='write.txt',mode='wb')
f.write('世界，你好'.encode('gbk'))
f.close()

#注意：w写一个文件时，会先把源文件清空，然后写入新内容