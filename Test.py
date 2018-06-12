# namespaceToParent = {'global':'none'}
# namespaceToVars = {'global':list()}
#
# def process(command, a1, a2):
#     if command == 'create':
#         create(a1, a2)
#     elif command == 'add':
#         add(a1, a2)
#     else:
#         return get(a1, a2)
#
# def create(namespace, parent):
#     namespaceToParent[namespace] = parent
#     namespaceToVars[namespace] = list()
#
# def add(namespace, var):
#     namespaceToVars[namespace].append(var)
#
# def get(namespace, var):
#     if namespace == 'none':
#         return 'None'
#     if var in namespaceToVars[namespace]:
#         return namespace
#     return get(namespaceToParent[namespace], var)
#
# n = int(input())
# for i in range(n):
#     command, a1, a2 = input().split()
#     res = process(command, a1, a2)
#     if res is not None:
#         print(res)
#
#


class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1

a = A()
print(a.val)

a.foo()
print(a.val)
