import json

def champions(name):
	with open("champions.json") as file:
		data = json.load(file)
	for champs in data["champions"]:
		if name == champs["name"]:
			return champs
	return "No champion found"