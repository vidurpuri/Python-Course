import requests

r = requests.get('https://api.github.com/users/vidurpuri')

with open('user_data.json', 'w') as f:
    f.writelines(r.text)
