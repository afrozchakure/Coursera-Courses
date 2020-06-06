import urllib.request, urllib.parse, urllib.error
import json
import ssl

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
connection = urllib.request.urlopen(url, context = ctx).read()
data = connection.decode()

info = json.loads(data)
print('User count:', len(info))
# print(info)
sum_count = 0
for item in info['comments']:
    # print(item['count'])
    sum_count += item['count']
    # print('Name', item['name'])
    # print('Id', item['id'])
    # print('Attribute', item['x'])
print(sum_count)