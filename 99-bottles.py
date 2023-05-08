for i in range(3,0,-1):
	bt= lambda j: f"{j} bottle{'s' if j-1 else ''}"
	w= lambda k: f" of beer{' on the wall' if k else ''}"
	btw=lambda j,k: bt(j) + w(k)
	print(
f"""{btw(i,1)}
{btw(i,0)}
Take one down, pass it around
{btw(i-1,1)}
""")
