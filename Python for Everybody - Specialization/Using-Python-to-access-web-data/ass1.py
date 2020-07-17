import re
fname = open('regex_sum_566858.txt')

a = re.findall('[0-9]+', fname.read())
a = [int(i) for i in a]
print(sum(a))
      
