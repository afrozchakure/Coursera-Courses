import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')  # Ask user for a url
html = urllib.request.urlopen(url, context=ctx).read()  # It all comes in form of a string
soup = BeautifulSoup(html, 'html.parser')  # It gives us a soup object (Takes nasty HTML and cleans it)

# Retrieve all of the anchor tags
tags = soup('a')  # Give a list of all anchor tags in the document (<a> </a> -- anchor tag)
for tag in tags:
    print(tag.get('href', None))  # It pull out all tags with href and prints its contents
    
# Input
# http://www.dr-chuck.com/page1.htm
# https://www.si.unich.edu/
print(html)
