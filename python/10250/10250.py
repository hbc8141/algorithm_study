count = int(input())

roomNumbers = list()

for index in range(count):
    data = list(map(int, input().split()))
    # 층수
    H = int(data[0])
    # 층별 방 수
    W = int(data[1])
    # 몇 번째 손님
    N = int(data[2])
    
    # H = 6
    # W = 12
    # N = 12
    floor = N%H

    if floor == 0:
        floor = H

    room = N/H+1 if N%H > 0 else N/H
    
    roomNumber = "{0:01d}{1:02d}".format(floor, int(room))

    roomNumbers.append(roomNumber)
    
for room in roomNumbers:
    print(room)