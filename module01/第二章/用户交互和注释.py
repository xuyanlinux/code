# name = input("Name:")
# age = input("Age:")
# job = input("Job:")
# hometown = input("Hometown:")
#
# info = '''-------------info of %s----------------
# "Name:"         %s
# "Age:"          %s
# "Job:"          %s
# "Hometown:"     %s
# ----------------END----------------------
# '''% (name,name,age,job,hometown)
#
# print(info)

#
# a = 11
# b = 2
# print(a/b)
# print(a%b)
# print(a//b)

# score = int(input("Please input ur score:"))
# if score >100 or score < 0:
#     print("Input your score between 0 and 100!")
# elif score > 89 and score <= 100:
#     print("A")
# elif score > 79 and score < 90:
#     print("B")
# elif score > 59 and score < 80:
#     print("C")
# elif score > 39 and score < 60:
#     print("D")
# else:
#     print("E")

# count = 0
#
# while count <= 100:
#     if count == 50:
#         pass
#     elif count >= 60 and count <=80:
#         print(count ** 2)
#     else:
#         print("loop ",count)
#     count += 1
#
# print("--------end-----------")
#

# age = 22
#
# count = 0
# 10
# while count < 3:
#     guess = int(input("Please input the age:"))
#     if age == guess:
#         print("bingo,you get it!")
#         break
#     elif age > guess:
#         print("try bigger!")
#     else:
#         print("try smaller!")
#     count+=1

age = 22
count = 0
while count < 3:
    guess = int(input("Please input the age:"))
    if age == guess:
        print("bingo,you get it!")
        break
    elif age > guess:
        print("try bigger!")
    else:
        print("try smaller!")
    count+=1
    if count == 3:
        re_or_not = input("one more chance? Please input 'yes' or 'no':")


        if re_or_not == 'yes':
            count =0