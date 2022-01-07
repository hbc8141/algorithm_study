maxIndex = 0
maxValue = 0

for index in range(1,10):
    number = int(input())
    
    if maxValue < number:
        maxIndex = index
        maxValue = number

print(maxValue)
print(maxIndex)