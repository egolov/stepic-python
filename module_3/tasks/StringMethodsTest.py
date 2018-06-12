from module_3.tasks.strings_methods import find_operations_count, instances_count

print(instances_count('abababa', 'aba'))
print(instances_count('abababa', 'abc'))
print(instances_count('abc', 'abc'))
print(instances_count('abcabcabcabc', 'abc'))
print(instances_count('aaaaa', 'a'))


# print(find_operations_count("ababa", "a", "b"))
# print(find_operations_count("ababa", "b", "a"))
# print(find_operations_count("ababa", "c", "c"))
# print(find_operations_count("ababac", "c", "c"))
# print(find_operations_count("abab", "ab", "ba"))