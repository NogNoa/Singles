for i in range(3,0,-1):
	bt= lambda j: "bottle" + "s" * bool(j-1)
	br="of beer"
	w="on the wall"
	print(
f"""{i} {bt(i)} {br} {w}
{i} {bt(i)} {br}
Take one down, pass it around
{i-1} {bt(i-1)} {br} {w}
""")
