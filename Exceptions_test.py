from Exceptions import fillInheritanceMap, mayBeSkipped

parents = dict()
fillInheritanceMap("A", parents)
fillInheritanceMap("B : A", parents)
fillInheritanceMap("C : B", parents)
fillInheritanceMap("D : C", parents)

print(parents)

s = {'A'}
print(mayBeSkipped('B', parents, s))
print(mayBeSkipped('C', parents, s))
print(mayBeSkipped('D', parents, s))

# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError
# catchedBefore = set()
# print(mayBeSkipped('ZeroDivisionError', parents, catchedBefore))
# catchedBefore.add('ZeroDivisionError')
#
# print(mayBeSkipped('OSError', parents, catchedBefore))
# catchedBefore.add('OSError')
#
# print(mayBeSkipped('ArithmeticError', parents, catchedBefore))
# catchedBefore.add('ArithmeticError')
#
# print(mayBeSkipped('FileNotFoundError', parents, catchedBefore))
# catchedBefore.add('FileNotFoundError')