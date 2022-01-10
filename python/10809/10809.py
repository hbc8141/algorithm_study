word = input()

# 아스키코드 97~123번까지 추가
alphabet = list(range(97,123))

for x in alphabet:
    # 해당하는 단어 찾기
    print(word.find(chr(x)))