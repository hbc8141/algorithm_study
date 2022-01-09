count = int(input())

studentScores = list()

for _ in range(count):
    scores = list(map(int, input().split()))
    average = sum(scores[1:])/scores[0]
    studentCount = 0
    
    for score in scores[1:]:
        if score > average:
            studentCount += 1
    
    rate = studentCount/scores[0]*100
    print("%.3f%%" % rate)