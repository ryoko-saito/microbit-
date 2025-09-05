l = [3,6,2,9,1]

# l内の値を小さい順に並べ替える
#目標 [1,2,3,6,9]
for i in range(4):
    for v in range(4):
        t = l[v]
        if l[v] > l[v+1]:
            l[v] = l[v+1]
            l[v+1] = t
print(l)
