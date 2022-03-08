def genfib(place, deg=1):
	if place == 0:
		return 1
	elif place < 0:
		return 0
	else:
		return genfib(place-1, deg) + genfib(place - 1 - deg, deg)
