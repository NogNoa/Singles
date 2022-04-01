def genfib(place, deg=1):
	def degfib(place):
		if place == 0:
			return 1
		elif place < 0:
			return 0
		else:
			return degfib(place-1) + degfib(place - 1 - deg)
	return degfib(place)
