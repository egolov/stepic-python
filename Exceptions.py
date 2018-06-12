def fillInheritanceMap(input, map):
    if ":" in input:
        ex, parents = input.split(" : ")
        split = parents.split()
        map[ex] = split
        for parent in split:
            if parent not in map:
                map[parent] = None
    else:
        map[input] = None

def mayBeSkipped(ex, parentsMap, catchedBefore):
    if ex in catchedBefore:
        return True

    parents = parentsMap[ex]
    if parents is None:
        return False

    for p in parents:
        if mayBeSkipped(p, parentsMap, catchedBefore):
            return True

    return False

# def mayBeSkipped

if __name__ == '__main__':
    parents = dict()
    n = int(input())
    for i in range(n):
        fillInheritanceMap(input(), parents)
    m = int(input())

    catchedBefore = set()
    skipList = list()
    for i in range(m):
        ex = input()
        if mayBeSkipped(ex, parents, catchedBefore):
            skipList.append(ex)
        catchedBefore.add(ex)

    for ex in skipList:
        print(ex)





