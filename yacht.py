from microbit import*

mat = [
        [0,0,9,0,0,0,0,0,0,0],
        [0,0,9,9,9,0,0,0,0,0],
        [0,0,9,0,0,0,0,0,0,0],
        [9,9,9,9,9,0,0,0,0,0],
        [0,9,9,9,0,0,0,0,0,0],
        ]

icons = []

while True:
    coord=""
    for vec in mat:
        i =0
        for v in vec:
            coord += str(v)
            i +=1
            if i > 4:
                break
        coord +=":"

        yacht = Image(coord)
        display.show(yacht)
        sleep(1000)

        for row in range(0,len(mat)):
                mat[row][len(mat[0])-1] = mat[row][0]
                for col in range(0,len(mat[0])-1):
                    mat[row][col] = mat[row][col+1]
