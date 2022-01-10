sentense = input()

words = [word.upper() for word in sentense]
alphabets = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in words:
    index = ord(word)-65
    alphabets[index] += 1

if alphabets.count(max(alphabets)) > 1:
    print("?")
else:
    print(chr(alphabets.index(max(alphabets))+65))