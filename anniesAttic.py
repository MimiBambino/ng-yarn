import urllib2
import json

response = urllib2.urlopen("https://www.kimonolabs.com/api/699jdals?apikey=T76wbONgzAL37suvbpw3KiyhyPNno69u")

big_data = json.load(response)

yarns = big_data["collection1"]

with open("data.json") as old_file:
    yarn_list = json.load(old_file) 

for item in range(len(yarns)):
	yarn = {}
	yarn["manufacturer"] = yarns[item]["line"] # Find substring up to first space in line value.
	yarn["price"] = yarns[item]["price"] # Strip the $ from price
	yarn["link"] = yarns[item]["link"]
	yarn["image"] = yarns[item]["image"]
	yarn["line"] = yarns[item]["line"] # Take substring of line after first space
	yarn["fiber"] = yarns[item]["fiber"]
	yarn["weight"] = yarns[item]["weight"]

	yarn_list.append(yarn)

for item in range(len(yarn_list)):
	if yarn_list[item]["weight"] == "Chunky":
		yarn_list[item]["weight"] = "Bulky"
	if yarn_list[item]["weight"] == "Super Chunky":
		yarn_list[item]["weight"] = "Super Bulky":

if len(yarn_list) > 50:
	with open('data.json', 'w') as outfile:
   		json.dump(yarn_list, outfile)



