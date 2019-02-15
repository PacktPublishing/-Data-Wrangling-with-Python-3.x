import sqlite3
conn = sqlite3.connect('employee.db')

c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS employee (name VARCHAR,hire_date VARCHAR,salary  VARCHAR,hobby VARCHAR,first_child_name VARCHAR)")

import json
with open ('hrdata1.json') as f:
    data = json.load(f)

for i in data:
    c.execute("INSERT INTO employee (name,hire_date,salary,hobby,first_child_name) VALUES (?,?,?,?,?)",(i['Name of Employee'],i['Hire Date'],i['Salary'],i['hobbies'][0],i['children'][0]['firstName']))

conn.commit()























