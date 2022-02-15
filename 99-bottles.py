for i in range(3,0,-1):
	bt= lambda j: "bottle" + "s" * bool(j-1)
	w= lambda j: " of beer" + " on the wall" * bool(j)
	btw=lambda j,k: bt(j) + w(k)
	print(
f"""{i} {btw(i,1)}
{i} {btw(i,0)}
Take one down, pass it around
{i-1} {btw(i-1,1)}
""")
