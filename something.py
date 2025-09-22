strings = ["AMC12", "H5SJS", "KYZU9", "1T3G5", "C4SFRD"]
print(list(filter(lambda x: len(x) == 5 and x[1].isdigit() and not x[2].isdigit(), strings)))