from pprint import pprint
import requests
import json

def heroes1():
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
#создадим словарь, в котором будет находиться информация о интеллекте каждого героя (изначально 0)
    intelligence_dict = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    
    for hero in heroes_list:
        response = requests.get(url,timeout=3)
        if response.status_code == 200:
            print(f'Ищем информацию по - {hero}')
        else:
            print("Ошибка")
        all_heroes = response.json()
        for h1 in all_heroes:
            if h1['name'] == hero: 
                intelligence_dict[hero] = int(h1['powerstats']['intelligence'])
            
    pprint(intelligence_dict)
    intelligence_max = max(intelligence_dict, key=intelligence_dict.get)
    print(f'Самый умный супергерой - {intelligence_max}')

if __name__ == '__main__':
    heroes1()