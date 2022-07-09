edges = [[1,2],[5,1],[1,3],[1,4]]
son1 = 0
son2 = 0
mantiq = False
for i in edges:
    for j in i:
        if son1 == 0:
            son1 = j
        elif son1 != 0 and son2 == 0: son2 = j
        elif j == son1:
            mantiq = True
            print(j)
            break
        elif j == son2:
            mantiq = True
            print(j)
            break
    if mantiq:
        break
        