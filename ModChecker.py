def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod_3 = mod_checker(3)
print(mod_3(3))
print(mod_3(6))
print(mod_3(9))
print(mod_3(10))

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))


f = open('./Buffer.py', 'r')
print(f.readline().rstrip())