for i in range(3,0,-1):
	bottles= "bottle" + "s" * bool(i-1)
	print(
f"""{i} {bottles} of beer on the wall
{i} {bottles} of beer
Take one down, pass it around
{i-1} bottles of beer on the wall
""")
