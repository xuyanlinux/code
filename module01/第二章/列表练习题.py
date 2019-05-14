#Author:Timmy
names = ["old_driver","rain","jack","shanshan","peiqi","black_girl"]
print(names)

names.insert(-1,"alex")
print(names)

names[names.index("shanshan")] = "姗姗"
print(names)

names.insert(2,["oldboy","oldgirl"])
print(names)

print(names.index("peiqi"))

new_list = [1,2,3,4,2,5,6,2]
names.extend(new_list)
print(names)

print(names[4:8])

print(names[2:11:2])

print(names[-3:])

# count = 0
# for i in names:
#     print(count,i);
#     count += 1
for index,name in enumerate(names):
    print(index,name)

# for i in names:
#     if count % 2 == 0:
#         i = -1
#     print(count,i);
#     count += 1
#
# index_2_first = names.index(2)
# index_2_second = names.index(2,index_2_first+1)
# print(index_2_second)
#
# products = [["iphone8",6888],["MacPro",14800],["小米6",2499],["Coffee",31],['Book',80],['Nike Shoes',799]]
# print("------------商品列表------------")
# for i in products:
#     print(str(products.index(i))+"."+i[0],i[1])


print(id(names))
print(id(names[0]))
print(id(names[1]))


