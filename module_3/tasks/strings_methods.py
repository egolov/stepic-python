def find_operations_count(s, a, b):
    if a in s and a in b:
        return -1

    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1

    return count

def instances_count(src, check):
    """
    src - string to check in
    check- string to check
    """
    count = 0
    start = 0
    pos = src.find(check)
    while pos >= 0:
        count += 1
        # src = src.replace(check, '', 1)
        start += 1
        pos = src.find(check, pos + 1)
    return count


if __name__ == '__main__':
    # s = input()
    # a = input()
    # b = input()
    # res = find_operations_count(s, a, b)
    # if res < 0:
    #     print('Impossible')
    # else:
    #     print(res)
    s = input()
    t = input()
    print(instances_count(s, t))