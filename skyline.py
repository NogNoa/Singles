class tower():
	def __init__(start,end,hight):
		self.start=start
		self.end=end
		self.hight=hight

	def __len__():
		return self.end - self.start

def skyline(towlist: list[tower]):
	terminal = max([tower.end for tower in towlist])
	begin = [[] for range(terminal)]
	for tower in towlist:
		begin[tower.start].(append(tower.hight).len(tower))
	stack=[]
	for pl, towi in swap:
		for tower in towi:
			if tower in stack:
				stack.pop(tower)
			else:
				stack.append(tower)





