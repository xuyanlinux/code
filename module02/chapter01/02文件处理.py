
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

lis_info_sta = ['3','4','age','phone','dept','enroll_date']
str ='1,Alex Li,22,13651054608,IT,2013-04-01'

dic_info = dict(zip(lis_info_sta,str.split(',')))
for key in lis_info_sta:
    if lis_info_sta.index(key) == len(lis_info_sta)-1:
        print(dic_info[key])
    else:
        print(dic_info[key],end=',')


st = lis_info_sta[0]+'>'+lis_info_sta[1]
print(st)
flag = eval(st)

print(flag)