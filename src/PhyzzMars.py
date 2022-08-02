class PhyzzMars:
	# TODO: add all the units and add more question keywords
	UNITS = {"m": "distance", "s": "time", "m/s": "velocity", "m/s2": "acceleration"}
	QUESTION_KEYWORDS = ["what", "determine", "calculate", "find"]
	FORMULAS = [
		{
			"givens": ["acceleration", "time"],
			"unknowns": ["distance"],
			"solution": "0.5*acceleration*time**2"
		},
		{
			"givens": ["distance", "time"],
			"unknowns": ["acceleration"],
			"solution": "2*distance/time**2"
		},
		{
			"givens": ["acceleration", "distance"],
			"unknowns": ["time"],
			"solution": "(2*distance/acceleration)**(1/2)"
		}
	]


	def __init__(self, text):
		self.text = text
		self.givens = {}
		self.unknowns = []


	# TODO: add more
	# convert everything to standard units and change the format if necessary
	def correct_format(self):
		return self.text.replace("seconds", "s").replace("meters", "m")


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
		
		self.givens = {self.UNITS[unit]: number for (unit, number) in zip(units, numbers)}

		if not self.givens or not self.unknowns:
			raise ValueError("Could not parse the text")

		return self.givens, self.unknowns


	def solve(self):
		if self.givens and self.unknowns:
			print(self.givens, self.unknowns)
			for formula in self.FORMULAS:
				givens = list(self.givens.keys())
				if formula["givens"] == givens and formula["unknowns"] == self.unknowns:
					solution = formula["solution"]
					for given in givens:
						solution = solution.replace(given, str(self.givens[given]))
					result = eval(solution)
					print(result)
					return result


		else:
			self.parse()
			self.solve()

