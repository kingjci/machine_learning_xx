# xx
#  数组索引
import numpy as np
# a = np.arange(10)**3
# print(a)
# print(a[2])
# print(a[2:5])   #2-4个
# a[:6:2] = -1000
# print(a)
# print(a[: :-1])
# for i in a:
#     print(i**(1/3))

def f(x,y):
    return 10*x + y
b = np.fromfunction(f,(5,4),dtype = int)
print(b)
print(b[2,3])
print(b[0:5,1])
print(b[:,1])
print(b[1:3,:])
print(b[-1])  # 最后一行
for row in b:   #对行操作
    print(row)
for element in b.flat:
    print(element)