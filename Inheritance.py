def readInheritance(input, parents):
    if ':' in input:
        clazz, parentsStr = input.split(' : ')
        parentsClasses = parentsStr.split()
        parents[clazz] = parentsClasses
        for p in parentsClasses:
            if p not in parents:
                parents[p] = None
    else:
        parents[input] = None


def isParent(parent, child, parents):
    classParents = parents[child]
    if child == parent:
        return True
    elif classParents is None:
        return False
    elif parent in classParents:
        return True
    else:
        for cl in classParents:
            if isParent(parent, cl, parents):
                return True
    return False


if __name__ == '__main__':
    parents = dict()
    n = int(input())
    for i in range(n):
        readInheritance(input(), parents)

    q = int(input())
    for i in range(q):
        cl1, cl2 = input().split()
        if isParent(cl1, cl2, parents):
            print('Yes')
        else:
            print('No')

