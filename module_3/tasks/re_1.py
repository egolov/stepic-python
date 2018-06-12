import re

#  вхождение 'cat' более двух раз
pattern_1 = r".*cat.*cat"
pattern_2 = r"cat"

print(re.match(pattern_1, "abc cat and cat abc")) # is not None
print(re.findall(pattern_2, "abc cat and cat abc")) # len() > 1
