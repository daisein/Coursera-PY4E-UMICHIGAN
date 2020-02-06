fh = open('romeo.txt')
allwords= list()
for line in fh:
    words = line.split()
    for word in words:
        if not word in allwords:
            allwords.append(word)
allwords.sort()

print(allwords)
