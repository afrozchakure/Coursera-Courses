import json
input = '''[
    {
    "id": "001",
    "x": "2",
    "name": "Chuck"
    },
    {
        "id": "009",
        "x": "7",
        "name": "Chuck"
    }
]'''  # This a python list

# JSON represents data as nested "lists" and "dictionaries"

info = json.loads(input)  # Info is not an object, but a list
print('User count:', len(info))  # Since it is a list, we can find the length
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])