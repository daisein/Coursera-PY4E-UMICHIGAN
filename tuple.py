# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.

# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


# get hours
hours = list()
fh = open('mbox-short.txt')
for line in fh:
    if 'From ' in line:
        # get the hour
        hours.append(line.rstrip().split(' ')[6].split(':')[0])
# print(hours)


# make a dictionary
hourcounts = dict()
for hour in hours:
    if hour not in hourcounts:
        hourcounts[hour] = 0
    if hour in hourcounts:
        hourcounts[hour] += 1
# print(hourcounts)

# desired output
desop = sorted ( [ (k,v) for k,v in hourcounts.items()] )
for (thing) in desop:
    print(str(thing[0]) + " "+ str(thing[1]))
