a =90
print("{0:b} {0:c} {0:d} {0:o} {0:x} {0:X}".format(a))
try:
    name = eval(input("请输入一个整数："))
    print(name*2)
except NameError:
    print("请输入一个整数：")
