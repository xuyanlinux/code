# score = float(input("输入你的成绩>>>>"))
# if score < 0 or score > 100:
#     print("成绩范围是0---100")
# elif score > 89:
#     print("成绩分类：A")
# elif score > 79:
#     print("成绩分类：B")
# elif score > 59:
#     print("成绩分类：C")
# elif score > 39:
#     print("成绩分类：D")
# else:
#     print("成绩分类：E")
import random
score = random.randint(0,100)
# print("你的成绩是：%s" % ( score ) )
# if score < 0 or score > 100:
#     print("成绩范围是0---100")
# elif score > 89:
#     print("成绩分类：A")
# elif score > 79:
#     print("成绩分类：B")
# elif score > 59:
#     print("成绩分类：C")
# elif score > 39:
#     print("成绩分类：D")
# else:
#     print("成绩分类：E")

names = []
names.append('alex')
nums = [0,1,2,3,4,5,6]

# for i in nums:
#     print(i)

st1 = 'xy'
st2 = 'yangyan'

st3 = '''{name}'s info 
name:   {name}
age:    {age}
'''
print(st3)
print(st3.format(name = 'xy', age = 32))

