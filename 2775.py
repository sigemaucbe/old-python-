a = int(input())
for i in range(a):
    #k는 몇층인지 나타냄
    #n는 몇호인지 나타냄
    FloorAndRoom = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
    for v in range(1,15):
        FloorAndRoom.append([1])
        for h in range(1,14):
            FloorAndRoom[v].append(FloorAndRoom[v][h-1]+FloorAndRoom[v-1][h])
    k = int(input())
    n = int(input())
    print(FloorAndRoom[k][n-1])