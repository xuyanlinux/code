#Author:Timmy

#元组：不可以修改
tu1 = (1,2,3,['a','b'],4,5)

#但是子列表是可以修改的

tu1[3][0] = 'A'
print(tu1)