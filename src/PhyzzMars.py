class PhyzzMars:

	# TODO: add all the units and add more question keywords
	UNITS = {"m": "distance", "s": "time", "m/s": "velocity", "m/s2": "acceleration"}
	QUESTION_KEYWORDS = ["what", "determine"]


	def __init__(self, text):
		self.text = text
		self.givens = {}
		self.unknowns = []


	# TODO: add more
	# convert everything to standard units and change the format if necessary
	def correct_format(self):
		return self.text.replace("seconds", "s").replace("meters", "m")


	# parse the text to get the givens and unknowns 
	def parse(self):

		text = self.correct_format()
		words = text.split()
		next_unknown = False

		units = []
		numbers = []

		for word in words:
			try: numbers.append(float(word))
			except:
				word = word.replace(".", "").replace(",", "").lower()
				if word in self.UNITS: units.append(word)
				if word in list(self.UNITS.values()):
					if next_unknown:
						self.unknowns.append(word)
						next_unknown = False
				if word in self.QUESTION_KEYWORDS: next_unknown = True
		
		self.givens = {unit: number for (unit, number) in zip(units, numbers)}

		return self.givens, self.unknowns

