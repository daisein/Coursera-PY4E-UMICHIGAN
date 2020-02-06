    fh = open('romeo.txt')
    allwords= list()
    for line in fh:
        words = line.split()
        # allwords.append(words)
        allwords += words
        allwords = list(dict.fromkeys(allwords))
    allwords.sort()
    print(allwords)
