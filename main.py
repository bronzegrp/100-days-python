import requests

my_chords = {'latitude':20.70515495954519,'longitude' :-100.44581134777364}
print(my_chords.keys())

url = 'http://api.open-notify.org/iss-now.json'

print(url)

iss = requests.get(url=url)
print('\n')
print(f'ISS INFO BELOW ->')
print(iss.json())
#learn git u skibidi


