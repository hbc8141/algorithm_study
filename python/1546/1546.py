subjectCount = int(input())
maxScore = 0
scores = list(map(int, input().split()))

scoreSum = 0

for score in scores:    
    if maxScore < score:
        maxScore = score

for index in range(len(scores)):
    newScore = scores[index]/maxScore*100
    scores[index] = newScore
    scoreSum += newScore

print(scoreSum/subjectCount)