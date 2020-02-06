#7.1 Write a program that prompts for a file name,
#then opens that file and reads through the file,
#and print the contents of the file in upper case.

# fname = input("Enter file name: ")
# fh = open(fname)
# # for line in fh:
# #     line.upcase()
# #     print(line)

fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
