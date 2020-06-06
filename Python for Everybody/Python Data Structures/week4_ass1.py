fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip().split()
    for i in line:
    	if i in lst: continue
    	lst.append(i)
lst.sort()
print(lst)

