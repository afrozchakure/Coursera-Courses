import json
data = '''{  
    "name" : "Chuck",
    "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''  # Looks like a python dictionary

info = json.loads(data)  # Load from string (We get back an object)
print('Name:', info['name'])  # 'info' is a dictionary
print('Hide', info['email']['hide'])