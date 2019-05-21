
#读文件
# f = open(file="兼职白领学生空姐模特护士联系方式.txt",mode="r",encoding='gbk')
# data = f.read()
# print(data)
# f.close()

##如果不知道编码，可以直接转成二进制模式，
# f = open(file="兼职白领学生空姐模特护士联系方式.txt",mode="rb")
# data = f.read()
# print(data)   ##都出来的是二进制显示，所以网络传输/文本/图片等情景下可以使用这种模式
# f.close()

# 安装python第三方工具包 chardet
###windows cmd中执行pip install chardet即可
###使用chardet分析编码类型
# import chardet
# re = chardet.detect(data)
# print(re)

##根据分析的编码类型，解码后读取
# print(data.decode(encoding='gbk'))

## 逐行打印：注意直接打印时，每行后面会多一个空行
# f = open(file="兼职白领学生空姐模特护士联系方式.txt",mode="r",encoding='gbk')
# for line in f:
#     print(line.strip())
# f.close()
#
# lis_info_sta = ['id','name','age','phone','dept','enroll_date']
# str ='1,Alex Li,22,13651054608,IT,2013-04-01'
#
# dic_info = dict(zip(lis_info_sta,str.split(',')))

# for i in range(len(lis_info_sta)):
#     print(lis_info_sta[i],str.split(',')[i],end=' ')
# for key in lis_info_sta:
#     if lis_info_sta.index(key) == len(lis_info_sta)-1:
#         print(dic_info[key])
#     else:
#         print(dic_info[key],end=',')
#
#
# st = lis_info_sta[0]+'>'+lis_info_sta[1]
# print(st)
# flag = eval(st)
#
# print(flag)
# offset = -50
# f = open(file='staff_table',mode='rb')
# while True:
#     f.seek(offset, 2)  # seek(offset, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
#     lines = f.readlines()  # 读取文件指针范围内所有行
#     if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
#         last_line = lines[-1]  # 取最后一行
#         break
    # 如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
    # 所以off翻倍重新运行，直到readlines不止一行
#     offset *= 2
# f.close()
# print('最后一行为：' + last_line.decode())

str = 'update staff_table set name="Rain Wang" where name = "Alex Li"'
if '>=' in str or '<=' in str:
    str = str.replace('>=',' >= ')
    str = str.replace('<=',' <= ')
else:
    str = str.replace('=',' = ')
    str = str.replace('>',' > ')
    str = str.replace('<',' < ')
str = str.replace('  ',' ')
list_input = str.split(' ')
for index,i in enumerate(list_input):
    if '"' in i :
        list_input[index] = i+' '+list_input[index+1]
        del list_input[index+1]

print(str)
print(list_input)
