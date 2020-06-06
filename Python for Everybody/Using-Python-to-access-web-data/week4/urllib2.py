import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

# This pulls the whole HTML script of the html document
for line in fhand:
    print(line.decode().strip())
    
