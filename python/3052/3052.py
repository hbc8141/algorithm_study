numbers = list()

for _ in range(10):
    number = int(input())
    
    numbers.append(number%42)
    
numbers = list(set(numbers))

print(len(numbers))