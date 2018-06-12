import os
import os.path

def extSeeker(dir, ext, nameAdjuster = lambda x: x):
    ans = list()
    for curDir, dirs, files in os.walk(dir):
        if list(filter(lambda x: x.endswith(ext), files)):
            ans.append(nameAdjuster(curDir))
    return ans

def writeLines(lines, file):
    with open(file, 'w') as out:
        for line in lines:
            out.write(line + '\n')


nameAdjuster = lambda name: name.replace('/home/e-golov/Downloads/', '')
dirs = extSeeker("/home/e-golov/Downloads/main", '.py', nameAdjuster)
# dirs.sort()
# for dir in dirs:
#     print(dir)
dirs.sort()
writeLines(dirs, '/home/e-golov/tmp/out.txt')
# print(os.path.exists('fer.py'))