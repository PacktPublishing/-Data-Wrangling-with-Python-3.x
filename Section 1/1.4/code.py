import json
d = {
     'first_name':'jamshaid',
     'second_name' : 'sohail',
     'address' : 'Lahore Pakistan'
     }
json_object = json.dumps(d,indent = 0)
print(json_object)

with open('hrdata1.json') as f:
    data = json.load(f)
    
for i in data:
    print(i['Name of Employee'])
    print(i['Hire Date'])
    print(i['hobbies'][0])
    print(i['children'][0]['firstName'])
    print('\n')