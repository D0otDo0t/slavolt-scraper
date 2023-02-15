import requests
import webbrowser
import json

api = 'https://api.divolt.xyz'

#Fetches config file or creates one if it doesn't exist

try:
  with open('svs_config.json', 'r') as f:
    data = json.load(f) 
except:
  xtoken = input('Enter your Divolt x-session-token:')
  headers = {'x-session-token': xtoken}
  try:  
    response = requests.get(api + '/users/@me', headers=headers).json()
    user = response['_id']
  except:
    raise Exception('Error fetching user ID.\nCheck that your x-session-token is correct and current.')
  data = { 'xtoken': xtoken, 'user': user}
  with open('svs_config.json', 'w') as f: 
     json.dump(data, f)
 
headers = {'x-session-token': data['xtoken']}
user = data['user']

dlrequest = '/channels/01G9AZ9AMWDV227YA7FQ5RV8WB'
dluploadid = '01G9AZ9Q2R5VEGVPQ4H99C01YP'
dlupload = f'/channels/{dluploadid}'

print(
'''
WELCOME TO SLAVOLT SCRAPER

Please imput a link in the following format:

<url> <quality id>

Where <quality id> is equal to:
================================
| ID  | Quality                |
|-----+------------------------|
|  0  | 128 kbps MP3 or AAC    |
|  1  | 320 kbps MP3 or AAC    |
|  2  | 16 bit, 44.1 kHz (CD)  |
|  3  | 24 bit, ≤ 96 kHz       |
|  4  | 24 bit, ≤ 192 kHz      |
| n/a | best available quality |
================================

Example: https://www.deezer.com/en/album/305629827 3
''')

#Sends request message

link = '!dl ' + input()

data = {"content": link}

response = requests.post(api + dlrequest + '/messages', headers=headers, json=data).json()
try:
  msgid = response['_id']
except:
  raise Exception('Message failed to send')

print('Message sent')

#Searches through messages sent after msgid until it finds a matching reply

data = {'after': msgid,
        'sort': 'Oldest'}

requiredValue = False

while not requiredValue:
  print('Fetching Messages')
  response = requests.get(api + dlrequest + '/messages', headers=headers, params=data).json()
  for x in response:
    if 'mentions' in x and x['mentions'][0] == user:
      msgid = x['_id']
      requiredValue = True
      break
    else:
      print('Bot Reply ID match not found.')

print('Bot response found')

#fetches response msg and identifies download status or if an error has occured

requiredValue = False

while not requiredValue:     
  response = requests.get(api + dlrequest + '/messages/' + msgid, headers=headers).json()
  requiredValue = response['content'].endswith(f'<#{dluploadid}>')
  if not requiredValue:
    if 'error' in response['content'].lower():
      print(response['content'])
      raise Exception('Error occured with Download.')
    print(response['content'].split('\n')[1])

print('Upload complete! Acquiring download link.')

#fetches messages in upload channel, if a mention match is found then it opens download url in browser

data = {'sort': 'Newest'}

response = requests.get(api + dlupload + '/messages', headers=headers, params=data).json()

for x in response:
  if 'mentions' in x and x['mentions'][0] == user:
    index = x['embeds'][0]['description'].rfind(' ')
    print('Opening Download link in Browser:\n' +  x['embeds'][0]['description'][index+1:])
    webbrowser.open(x['embeds'][0]['description'][index+1:])
    break
  else:
    print('Upload match not found. Trying next message.')

