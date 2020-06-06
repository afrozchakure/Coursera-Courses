# Parsing XML
import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="int1">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
 </person>'''
 
tree = ET.fromstring(data)  # Pass the string and gives us a tree object of the data
print('Name:', tree.find('name').text)  # It gets the text 'Chuck'
print('Attr:', tree.find('email').get('hide'))  # It get the attribute 'yes'
