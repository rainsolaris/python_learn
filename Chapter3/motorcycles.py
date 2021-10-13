#! /usr/bin/env python3

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#替换 就是把列表对应的值直接替换就行了。
#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles_2 = []
motorcycles_2.append("honda")
motorcycles_2.append("yamaha")
motorcycles_2.append("suzuki")
motorcycles_2.append("ducati")
print(motorcycles_2)

print("--------")
motorcycles_3 = ['honda', 'yamaha', 'suzuki']
motorcycles_3.insert(0,'ducati')
print(motorcycles_3)
del motorcycles_3[0]
print(motorcycles_3)
print("--------")

print(motorcycles_3)
poped_motorcycles = motorcycles_3.pop()
print(poped_motorcycles)

print("--------")

