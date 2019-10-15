# import copy
# class C():
#     def __init__(self):
#         self.x = [1]
#         self.y = [2]
#     def __repr__(self):
#         return f'{self.x},{self.y}'
# c = C()
# list=[]
# for i in range(10):
#     list.append(c)
#
# for i in list:
#     i=copy.deepcopy(i)
#
# list[7].x.append(10)
# print(list[0])
# d = copy.deepcopy(c)
# d.x[0] = 3
# print(c)
# print(d)

