import json

class Config():
	def __init__(self):
		with open("config.json") as file:
			config = json.load(file)
			self.token = config["config"]["token"]