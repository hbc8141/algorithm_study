indexs = [0,0,0,0,0,0,0,0,0,0]
value = 1

for _ in range(3):
    value *= int(input())
    
splitNumber = [int(value) for value in str(value)]

for number in splitNumber:
    indexs[number] += 1

for index in indexs:
    print(index)