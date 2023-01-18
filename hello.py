# 0000*0000
# 000*0*000
# 00*0*0*00
# 0*0*0*0*0
# *0*0*0*0*

# dont care about rhs 0s
# dims : n rows | n-1 0s max

# def stars(rows):
#     for row in range(rows):
#         for zero in range(rows-row-1):
#             # print(" ", end="")
#             print(end=" ")
#         for star in range(row+1):
#             print("*", end=" ")
#         print()

# print(stars(5))

#s="I am learning python"
# print(s[::-1])
# print(s.find("am"))

# find vs index: 
# if find cannot find str it returns -1 | index returns errors used in exception handling

# print(s.find("a", 5, ))

# arr = ["a", "b", "c"]
# print(" ".join(arr))

# print("{:5d}".format(12))
# print("{:2d}".format(1234))
# print("{:8.3f}".format(12.2345))
# print("{:05d}".format(12))
# print("{:^10.3f}".format(12.2346))
# print("{:<05d}".format(12))
# print("{:>08.3f}".format(12.2346))
# print("{:=8.3f}".format(-12.2346))
# print("hello, my name is {name}, i am {years} years old".format(name="tanuj", years=21))

s = "i am learning python"
# mapp = {}
# for char in s:
#     if char ==" ":
#         continue
#     if char in mapp:
#         mapp[char]+=1
#     else:
#         mapp[char]=0
# print(mapp)       

# arr=[0]*26
# for char in s:
#     if char==" ":
#         continue
#     pos = ord(char)-ord("a")
#     arr[pos]+=1
# # print(arr)

# for i in range(len(arr)):
#     if arr[i]:
#         print("{alpha} : {freq}".format(alpha=(chr)(i+ord("a")), freq=arr[i]), end=", ")

# sorted : new object | x.sort() : changes x
# print(sorted(s))
# arr=[12,23,45]
# arr.extend((1,2,3)) # bigger append | accepts tuple
# arr.append(8)
# print(arr)
# arr.sort()
# print(arr)

# colors = dict()
# colors["red"]=1
# print(colors.get("d", "nothing"))

# colors.update({"x":1, "y":2}) : to add multiple key val pairs

# for keys in colors:
#     print(colors[keys])
# for keys in colors.keys():
#     print(colors[keys])
# for k,v in colors.items():
#     print(k)

# enumerate(colors) : returns iterator and keys
# l1 = ["a", "b", "c"]
# l2 = [1,2,3,4,5]
# d = dict(list(zip(l1, l2)))
# print(d)

# q = set()
# q.add(1)
# print(q)
# q.remove()

# q1 = {1,2,3}
# q2 = {2,3,4}
# print(q1.difference(q2))    # a-b
# print(q1.union(q2))
# print(q1.intersection(q2))
# print(q1.symmetric_difference(q2))  # U - (a intersection b)

# d={}
# d.update({"a":22, "b":12})
# print(sorted(d.values()))

# sort dict by values
# sorted(d.items(), key=lambda x: x[1])

# passing list to a func and changing it changes the og list

# def func(mylist):
#     mylist.append(100)

# mylist=[1,2]
# func(mylist)
# print(mylist)

# fact

# def fact(n):
#     if n<2:
#         return n
#     return (n)*fact(n-1)

# print(fact(5))

# s="tanuj"

# def rev(s, pos, ans):
#     if pos<0:
#         return ans
#     ans+=s[pos]
#     return rev(s, pos-1, ans)

# print(rev(s, len(s)-1, ""))

# lambda func
# f = lambda a,b : a+b
# print(f(1,2))

# x = input() # 1 2 3
# print(list(map(int,x.strip().split())))

# l = [1,2,3,4]
# print(list(map(lambda x:x**2, l)))
# print(list(filter(lambda x:x%2==0, l)))

# from functools import reduce
# print(reduce(lambda x,y:x+y, l))

# def solve(a,b,c,):
#     return a,b,c    # returns a tuple

# file handling
# mode = w | wt | wb | r | rt | rb | a | at : append | t : text mode (default) | + : r+w
# mode = "w"
# f = open("test.txt", mode)
# f.write("hello world \n")
# f.close()

# with open("test.txt", "w") as f:
#     f.write("hello ")
#     f.write("world")

# w overwrites | use a+ to update file

# with open("test.txt", "a") as f:
#     f.write("\nappended")

# with open("test.txt", "r") as f:
    # first_line = f.readline()
    # line = f.read() # whole file
    # line = f.read(15)
    # lines = f.readlines()   # list
# print(lines)

# with open("test.txt", "a+") as f:
#     f.seek(0,0) # start of file
#     # first arg :  pos in chr, bits | second arg : 0 : start of file | 1 : curr line | 2 : end of file
#     # f.write("this is python, ") # writes to end of file
#     # seek is used to read
#     # f.tell() # curr char pos
#     line = f.readline()
#     print(line)

# edit lines in a file

# with open("assignment.txt", "a+") as f:
#     for i in range(10):
#         f.write("line number {x} \n".format(x=i+1))

# edit = 1
# with open("assignment.txt", "a+") as f:
#     f.seek(0,0) # start of page
#     lis = f.readlines()
#     lis[edit] = "not my problem \n"
#     new = open("temp.txt", "w")
#     new.writelines(lis)
#     new.close()
# import os
# os.remove("test.txt")
# os.rename("temp.txt", "test.txt")
    