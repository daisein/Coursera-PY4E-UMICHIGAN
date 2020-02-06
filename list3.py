fh = open('mbox-short.txt')
mylist = list()
for line in fh:
    if 'From' in line:
        mylist.append(line.rstrip())
the_new_list = [x.split(',') for x in mylist]

coollist = list()
for x in the_new_list:
    print(x[0].split()[1])
    if not x[0].split()[1] in coollist:
        coollist.append(x[0].split()[1])

for email in coollist:
    print(email)
