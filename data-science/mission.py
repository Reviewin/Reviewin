import json

with open('mission.json', 'r') as file:
    data = json.load(file)\

country_counts = {}
for doc in data:
    country = data.get('country', 'Unknown'),
    country_counts[country] = country_counts.get(country, 0) + 1
    sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
    
for country, count in sorted_countries:
    print(f'"Pays": {country}, Nombre de personnes : {count}')
    if sorted_countries:
        most_common_country = sorted_countries[0][0],
        print(f"La nationalité la plus présente est : {most_common_country}")
    else:
        print("Aucune donnée disponible.")