'''
DOc strings
'''
import sys
import requests
import json
import csv

todo_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'

req = requests.get(todo_url) 
results = json.loads(req.text)

task = 0
completed_task_title = []

with open('USER_ID.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for result in results:
        users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(result['userId']))
        user = json.loads(users.text)

        writer.writerow([result['userId'], user['username'], result['completed'], result['title']])