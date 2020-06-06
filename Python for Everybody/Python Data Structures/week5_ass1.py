name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word_dict = {}
for line in handle:
    if line.startswith("From:"): continue
    if line.startswith("From"):
        line = line.split()[1]
        if line in word_dict:
            word_dict[line] += 1
        else:
			word_dict[line] = 1

email = None
max_count = None
for k in word_dict:
    if max_count is None or word_dict[k] > max_count:
		max_count = word_dict[k]
		email = k
print(email, max_count)
    

