strings = ["AMC12", "H5SJS", "KYZU9", "1T3G5", "C4SFRD"]
print(list(filter(lambda x: len(x) == 5 and x[1].isdigit() and not x[2].isdigit(), strings)))
s = "MRJ"
a = s[1:] * 2
b = a[:2] + s[0] + a[2:]
print(b)