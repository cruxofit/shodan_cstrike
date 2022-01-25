from shodan import Shodan
from pandas import DataFrame
api = Shodan("")
matches = []
cstrike_list = []
#First we filter out high-volume countries, then we search them 1x1
#This is implemented so I didn't hit my max results in a single search (1k)
country_list = ['CN','US','HK']
cstrike = api.search('product:Cobalt Strike Beacon !country:CN !country:HK !country:US',limit=1000)
for match in cstrike['matches']:
    matches.append(match)
for country in country_list:
    cstrike = api.search('product:Cobalt Strike Beacon country:{}'.format(country),limit=1000)
    for match in cstrike['matches']:
        matches.append(match)
for data in matches:
    cstrike_list.append(data)
df = DataFrame(cstrike_list)
#CSV will be large and messy. Try filtering data before writing.
df.to_csv('shodan_cstrike.csv', encoding='utf-8')
