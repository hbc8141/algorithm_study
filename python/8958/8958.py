count = int(input())
oxAnswers = list()

for _ in range(count):
    oxAnswers.append(input())

for answer in oxAnswers:
    oxAnswerChar = [a for a in answer]
    score = 0
    maxScore = 1

    for answer in oxAnswerChar:
        if answer == 'O':
            score += maxScore
            maxScore += 1
        else:
            maxScore = 1

    print(score)