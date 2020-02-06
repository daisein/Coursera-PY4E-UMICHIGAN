fh = open('mbox-short.txt')
mylist = list()
for line in fh:
    if 'From' in line and 'From:' not in line:
        mylist.append(line.rstrip())
the_new_list = [x.split(',') for x in mylist]


count = 0

for email in the_new_list:
    print(email[0].split(' ')[1])
    count += 1
print("There were " + str(count) + " lines in the file with From as the first word")
