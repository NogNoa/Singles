for i in range(3,0,-1):
	bottles= lambda j: "bottle" + "s" * bool(j-1)
	print(
f"""{i} {bottles(i)} of beer on the wall
{i} {bottles(i)} of beer
Take one down, pass it around
{i-1} {bottles(i-1)} of beer on the wall
""")
