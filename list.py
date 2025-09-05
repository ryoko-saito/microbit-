from microbit import *

mat = [
	[9,9,0,0,0],
	[0,9,0,0,0],
	[0,9,9,0,9],
	[9,9,9,9,9],
	[9,9,9,9,9]
]

icons = []
for i in range(0, len(mat)+1):
	coord = ""
	for vec in mat:
		for v in vec:
			coord += str(v)
		coord += ":"

	icons.append(Image(coord))

        for row in range(len(mat)-1,0,-1):
                mat[row] = mat[row-1]
        mat[0] = [0,0,0,0,0]

display.show(icons,delay=1000)
