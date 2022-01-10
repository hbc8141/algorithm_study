data = input().split()

# 곡의 개수
A = int(data[0])

# 평균값
I = int(data[1])

if A > 1:
    print((A * (I-1)) +1)
else:
    print(A*I)