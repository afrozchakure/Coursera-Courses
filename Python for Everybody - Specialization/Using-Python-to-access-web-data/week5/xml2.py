import xml.etree.ElementTree as ET
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)  # Takes in from outside world to inside world in python
lst = stuff.findall('users/user')  # Under 'users' find all 'user' tags (We get these tags in a list, in form of trees)
print('User count:', len(lst))  # We count how many there are
for item in lst:  # Takes successive values
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)  # Gets the text content under 'id'
    print('Attribute', item.get('x'))  # Get the attribute 'x' content in original user tag
