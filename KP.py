import urllib2
import json

response = urllib2.urlopen("https://api.import.io/store/connector/_magic?url=http%3A%2F%2Fwww.knitpicks.com%2Fyarns%2FAll_Knit_Picks_Yarn__L300198.html%3FshowAll%3Dyes&format=JSON&js=false&_apikey=f5ff65e0cafc423782b9c4a99faa57120b405f6116a70a9463a352a5cb9bbc86443c67f2471bb3616f9b99edfeea3b620e3736cc8b848ba2b46f839dd70aa4a0546692b3619cc1d3da9c17c0bdc33338")

big_data = json.load(response)

yarns = big_data["tables"][0]["results"]

yarn_list = []


for item in range(len(yarns)):
	yarn = {}
	yarn["manufacturer"] = "Knit Picks"
	yarn["price"] = yarns[item]["costsmall_value_prices"]
	yarn["link"] = yarns[item]["titlesmall_link"]
	yarn["image"] = yarns[item]["itemimglink_image"]
	yarn["line"] = yarns[item]["itemimglink_image/_alt"]
	yarn["fiber"] = yarns[item]["yarnweight_values"][0]
	yarn["weight"] = yarns[item]["yarnweight_values"][1]

	yarn_list.append(yarn)

if len(yarn_list) > 50:
	with open('data.json', 'w') as outfile:
   		json.dump(yarn_list, outfile)



