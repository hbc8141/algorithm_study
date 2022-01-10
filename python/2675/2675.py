count = int(input())

for _ in range(count):
    data = input().split()
    repeatCount = int(data[0])
    P = list()
    
    words = [char for char in data[1]]
    
    for word in words:
        for _ in range(repeatCount):
            P.append(word)
        
    print("".join(P))