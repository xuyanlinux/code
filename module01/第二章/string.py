#Author:Timmy
# a = 'Alex'
# print(a,id(a))
# a = 'Jack'
# print(a,id(a))

##如上所示，重新赋值并没有覆盖原先的内存地址，而是重新开辟了一块内存
##原先的内存，python会自动清理

s = 'Hello World!'
print(s.swapcase())