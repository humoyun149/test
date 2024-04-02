import json

with open('fixtures/regions.json', 'r',encoding='utf-8-sig') as file:
    regions = json.load(file)
    for i in regions:
        print(i)

