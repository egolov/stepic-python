from Inheritance import readInheritance, isParent
# 2
#
# A : C B
#
# B : D E
#
# 1
#
# E A
parents = {}
# readInheritance('A : C B', parents)
# readInheritance('B : D E', parents)
# print(parents)
# print(isParent('E', 'A', parents))
# print(isParent('A', 'B', parents))
# print(isParent('B', 'D', parents))
# print(isParent('C', 'D', parents))
# print(isParent('D', 'A', parents))

# classA : classB classC classD classG classH
# classB : classC classE classG classH classK classL
# classC : classE classD classH classK classL
# classE : classD classF classK classL
# classD : classG classH
# classF : classK
# classG : classF
# classH : classL
# classK : classH classL
# classL
# readInheritance('classA : classB classC classD classG classH', parents)
# readInheritance('classB : classC classE classG classH classK classL', parents)
# readInheritance('classC : classE classD classH classK classL', parents)
# readInheritance('classE : classD classF classK classL', parents)
# readInheritance('classD : classG classH', parents)
# readInheritance('classF : classK', parents)
# readInheritance('classG : classF', parents)
# readInheritance('classH : classL', parents)
# readInheritance('classK : classH classL', parents)
# readInheritance('classL', parents)
#
# print('Yes' if isParent('classK', 'classD', parents) else 'No')
# print('Yes' if isParent('classD', 'classA', parents) else 'No')
# print('Yes' if isParent('classG', 'classD', parents) else 'No')
# print('Yes' if isParent('classH', 'classA', parents) else 'No')
# print('Yes' if isParent('classE', 'classE', parents) else 'No')
# print('Yes' if isParent('classH', 'classG', parents) else 'No')
# print('Yes' if isParent('classE', 'classL', parents) else 'No')
# print('Yes' if isParent('classB', 'classD', parents) else 'No')
# print('Yes' if isParent('classD', 'classL', parents) else 'No')
# print('Yes' if isParent('classD', 'classG', parents) else 'No')
# print('Yes' if isParent('classD', 'classE', parents) else 'No')
# print('Yes' if isParent('classA', 'classF', parents) else 'No')
# print('Yes' if isParent('classA', 'classC', parents) else 'No')
# print('Yes' if isParent('classK', 'classA', parents) else 'No')
# print('Yes' if isParent('classA', 'classH', parents) else 'No')
# print('Yes' if isParent('classK', 'classD', parents) else 'No')
# print('Yes' if isParent('classH', 'classB', parents) else 'No')
# print('Yes' if isParent('classK', 'classB', parents) else 'No')
# print('Yes' if isParent('classD', 'classL', parents) else 'No')
# print('Yes' if isParent('classG', 'classG', parents) else 'No')
# print('Yes' if isParent('classA', 'classH', parents) else 'No')
# print('Yes' if isParent('classK', 'classL', parents) else 'No')
# print('Yes' if isParent('classG', 'classE', parents) else 'No')
# print('Yes' if isParent('classB', 'classA', parents) else 'No')
# print('Yes' if isParent('classC', 'classK', parents) else 'No')
# print('Yes' if isParent('classK', 'classL', parents) else 'No')
# print('Yes' if isParent('classC', 'classL', parents) else 'No')
# print('Yes' if isParent('classG', 'classC', parents) else 'No')
# print('Yes' if isParent('classD', 'classD', parents) else 'No')
# print('Yes' if isParent('classC', 'classG', parents) else 'No')
# print('Yes' if isParent('classE', 'classA', parents) else 'No')
# print('Yes' if isParent('classF', 'classK', parents) else 'No')
# print('Yes' if isParent('classB', 'classG', parents) else 'No')
# print('Yes' if isParent('classH', 'classL', parents) else 'No')
# print('Yes' if isParent('classL', 'classF', parents) else 'No')
# print('Yes' if isParent('classH', 'classG', parents) else 'No')
# print('Yes' if isParent('classD', 'classA', parents) else 'No')
# print('Yes' if isParent('classH', 'classL', parents) else 'No')

readInheritance('A', parents)
readInheritance('X', parents)

readInheritance('B : A', parents)
readInheritance('C : A', parents)
readInheritance('Y : A', parents)
readInheritance('Y : A X', parents)
readInheritance('Z : X', parents)

readInheritance('D : B C', parents)
readInheritance('V : Y Z', parents)

readInheritance('E : D', parents)
readInheritance('F : D', parents)
readInheritance('W : V', parents)

readInheritance('G : F', parents)


print(isParent('A', 'A', parents))

print(parents)