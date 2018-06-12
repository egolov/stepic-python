def foo(inputFile, outputFile):
    with open(inputFile, 'r') as inp, open(outputFile, 'w') as out:
        iLines = list()
        for iLine in inp:
            iLine = iLine.rstrip()
            iLines.insert(0, iLine)
        for oLine in iLines:
            out.write(oLine + "\n")

foo('/home/e-golov/Downloads/dataset_24465_4.txt', '/home/e-golov/tmp/out.txt')