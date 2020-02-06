x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
import re
y = re.findall('@(\S+)', x)
print(y)
