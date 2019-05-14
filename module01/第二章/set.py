#Author:Timmy

# s = {1,2,3,4}
# l = [1,2,2,3,4]
# print(set([1,2,2,3,4]))

##集合关系测试
iphone7 = {'alex', 'rain','jack', 'old_driver'}
iphone8 = {'alex', 'shanshan', 'jack', 'old_boy'}

#交集
print(iphone7.intersection(iphone8))
print(iphone7 & iphone8)

#差集
print(iphone7 - iphone8)
print(iphone7.difference(iphone8))

#并集
print(iphone7.union(iphone8))
print(iphone7 | iphone8)

#对称差集
print(iphone7.symmetric_difference(iphone8))
print(iphone7 ^ iphone8)


iphone9 = {'rain'}
#是否相交
print(iphone8.isdisjoint(iphone9))
print(iphone7.isdisjoint(iphone9))

# 是否子集
print(iphone9.issubset(iphone7))
print(iphone9.issubset(iphone8))

# 是否超集
print(iphone7.issuperset(iphone9))
print(iphone8.issuperset(iphone9))

#判断一个元素是不是在集合中
print('rain' in iphone7)
print('rain' in iphone8)
print(iphone9 in iphone7)   # 这个是判断iphone9是不是iPhone7中的一个元素，而不是判断集合之间的sub与super关系

