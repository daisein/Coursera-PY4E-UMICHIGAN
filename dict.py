# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.

# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.

# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.

# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fh = open('mbox-short.txt')
mylist = list()
for line in fh:
    if 'From ' in line:
        y = line.rstrip().split()[1]
        mylist.append(y)

counts = dict()
for email in mylist:
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] += 1

bigkey = None
bigvalue = None

for key in counts:
    if bigvalue == None:
        bigvalue = counts[key]
        bigkey = key
    elif bigvalue < counts[key]:
        bigvalue = counts[key]
        bigkey = key

print(bigkey, bigvalue)
