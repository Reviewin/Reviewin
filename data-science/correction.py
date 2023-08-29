import matplotlib.pyplot as plt
import json


with open("mission.json", "r") as json_file:
    datas = json.load(json_file)
all_nationalities_occurences = {}
dict_country = {}
countries = []
for i in range(1,len(datas["rows"])-1):
    country = datas["rows"][i]["doc"]["country"]
    dict_country[country] = 0
    countries.append(country)
countings = []
for i in range(1,len(datas['rows'])-1):
    for j in range(1,len(datas["rows"])-1):
        if datas["rows"][i]["doc"]["country"] == datas["rows"][j]["doc"]["country"]:
            dict_country[datas["rows"][i]["doc"]["country"]] += 1
        else:
            pass

countingss = list(dict_country.values())
countriess = list(dict_country.keys())
print(countingss)
print(countriess)
print(len(dict_country))


#done_for = 0
#frequencies = []
#nationalities = []
#for i in range(len(datas["rows"])):
    #country = datas["rows"][i]["doc"]['country']
    #frequency = compter_occurrences(datas, datas["rows"][i]["doc"]["country"])
    #all_nationalities_occurences[datas["rows"][i]["doc"]['country']] = frequency
    #done_for = done_for + 1
    #frequencies.append(frequency)
    #nationalities.append(country)

plt.bar(countriess, countingss)
plt.xticks(countriess, rotation="horizontal",size=4)
plt.ylabel("Likes")
plt.xlabel("Countries")
plt.show()