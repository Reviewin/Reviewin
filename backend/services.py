
def services(database_name, payload: dict):
    database_name.save(payload)

import pycountry
from pycountry import countries
list_of_countries = []
for i in range(len(pycountry.countries)):
    list_of_countries.append(list(pycountry.countries)[i].name)
final_list_uppercase = []
for i in range(len(list_of_countries)):
    final_list_uppercase.append(list_of_countries[i].upper())
print(final_list_uppercase)

