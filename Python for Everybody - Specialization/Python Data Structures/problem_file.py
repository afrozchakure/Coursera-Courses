# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
spam = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count += 1
    spam += float(line[20:])
    #print(line[20:])
print("Average spam confidence:",spam / count)

