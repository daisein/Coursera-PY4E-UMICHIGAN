text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find('0')
print atpos
babe = float(text[atpos:])
print(babe)
