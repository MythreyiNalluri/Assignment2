fname = input("enter file name")
fh = open(fname)
lst = list()
for line in fh:
    word = line.rstrip().split()
    for element in word:
        lst.append(element)

counts = [print(lst.count(item), item) for item in set(lst)]
