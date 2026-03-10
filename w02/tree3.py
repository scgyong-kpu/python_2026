"""
재귀 호출로 나무를 그리되, 가지 길이뿐 아니라 각도와 색상에도 변화를 주어
더 자연스러운 나무를 만드는 예제.

`tree2.py`에서는 가지 길이에만 난수를 적용했지만,
이 파일에서는 다음 요소까지 함께 변화시킨다.
1. 왼쪽 가지와 오른쪽 가지의 갈라지는 각도
2. 가지 굵기에 따른 색상 계열
3. 같은 계열 안에서도 조금씩 달라지는 실제 색상

이렇게 하면 결과가 훨씬 덜 기계적이고,
줄기, 잔가지, 잎 부분이 시각적으로 구분되는 나무를 만들 수 있다.
"""

import turtle as t
import random

# 기본 가지 분기 각도
ANGLE = 20

# 가지 길이가 이 값보다 짧아지면 더 이상 갈라지지 않는다.
MIN_LENGTH = 5

# 하위 가지 길이는 부모 가지 길이의 70%로 줄어든다.
REDUCE_RATE = 0.7

# 가지 길이에 비례해 펜 두께를 정하는 비율
WIDTH_RATE = 0.1

# 난수 비율의 범위: 값에 약간의 흔들림을 준다.
RANDOM_RATE_MIN = 0.9
RANDOM_RATE_MAX = 1.1

# 나뭇잎, 잔가지, 굵은 줄기에 사용할 기본 색상
COLOR_LEAF  = (0.7, 0.5, 0.0)
COLOR_SPRIG = (0.4, 0.3, 0.1)
COLOR_BRANCH = (0.3, 0.1, 0.1)

def random_value(value):
	# 주어진 값에 난수를 곱해 약간씩 다른 결과가 나오게 만든다.
	return value * random.uniform(RANDOM_RATE_MIN, RANDOM_RATE_MAX)

def color_near(color):
	# 기준 색상 주변의 비슷한 색을 만들어 자연스러운 변화를 준다.
	r, g, b = color
	return (
		random_value(r),
		random_value(g),
		random_value(b)
	)

def tree(length):
	# 현재 가지 길이에도 약간의 난수를 적용해 더 자연스럽게 만든다.
	len = random_value(length)
	w = len * WIDTH_RATE

	# 가지 굵기에 따라 잎, 잔가지, 굵은 줄기의 색상을 다르게 준다.
	# 그리고 같은 계열 안에서도 조금씩 다른 색을 사용해 생동감을 높인다.
	if w < 1:
		t.color(color_near(COLOR_LEAF))
	elif w < 2:
		t.color(color_near(COLOR_SPRIG))
	else:
		t.color(color_near(COLOR_BRANCH))
	# print(w, t.pencolor())

	# 현재 가지 길이에 맞는 굵기로 줄기를 그린다.
	t.width(w)
	t.pendown()
	t.forward(len)

	# 가지가 충분히 길면 좌우로 하위 가지를 재귀적으로 만든다.
	if len > MIN_LENGTH:
		# 왼쪽과 오른쪽의 각도를 서로 다르게 랜덤화하면 더 자연스럽다.
		angle_left = random_value(ANGLE)
		angle_right = random_value(ANGLE)

		# 하위 가지는 더 짧아진다.
		sub = len * REDUCE_RATE

		# 왼쪽 가지를 그린다.
		t.left(angle_left)
		tree(sub)

		# 오른쪽 가지를 그리기 위해 반대 방향으로 회전한다.
		t.right(angle_left + angle_right)
		tree(sub)

		# 상위 호출의 방향을 유지하도록 원래 방향으로 되돌린다.
		t.left(angle_right)

	# 현재 호출이 시작된 위치로 되돌아가 상위 줄기에서 다음 가지를 이어 그릴 수 있게 한다.
	t.penup()
	t.backward(len)


# 그리는 과정을 빠르게 보기 위해 최고 속도로 설정한다.
t.speed(0)

# 창 제목을 설정한다.
t.title("재귀 호출로 나무 그리기 #3: 색상 요소 추가")


# 화면 아래쪽에서 시작해 위로 자라는 나무처럼 보이게 배치한다.
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)

# 길이 120의 줄기에서 시작하여 재귀적으로 나무 전체를 그린다.
tree(120)

t.exitonclick()  # 창을 클릭하면 종료
