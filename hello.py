score = input("Enter Score: ")
try:
    float(score)
except:
    print('gotta enter a number')
    exit()

if float(score) > 1.0:
    print('too large')
    exit()
elif float(score) < 0.0:
    print('negative doesnt make sense here')
    exit()
elif float(score) >= 0.9:
    print('A')
elif float(score) >= 0.8:
    print('B')
elif float(score) >= 0.7:
    print('C')
elif float(score) >= 0.6:
    print('D')
elif float(score) < 0.6:
    print('F')
