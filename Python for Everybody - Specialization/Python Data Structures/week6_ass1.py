name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours_dict = dict()
for line in handle:
    if line.startswith("From:"): continue
    if line.startswith("From"):
        line = line.split()
        #rint(line)
        hours = line[5][:2]
        hours_dict[hours] = hours_dict.get(hours, 0) + 1
list_hours = list()
for x, y in hours_dict.items():
    list_hours.append((x, y))
list_hours.sort()
#print(list_hours)
for x in list_hours:
    print(x[0], x[1])
        
