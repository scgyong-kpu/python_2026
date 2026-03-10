"""
재귀 호출로 나무를 그리되, 가지 길이에 약간의 난수를 섞어
더 자연스러운 나무 모양을 만드는 예제.

`tree1.py`에서는 모든 가지가 같은 비율로 정확히 줄어들었기 때문에
전체 모양이 규칙적이고 대칭적으로 보였다.
이 파일은 각 가지 길이에 작은 무작위 변화를 주어,
실제 나무처럼 조금씩 다른 길이와 균형을 가지게 만든다.

즉, 기본 재귀 구조는 그대로 유지하면서
"같은 규칙에 작은 변화를 더하면 훨씬 자연스러운 결과가 나온다"는 점을 보여준다.
"""

import turtle as t
import random

# 가지가 좌우로 갈라질 때 사용하는 기본 회전 각도
ANGLE = 20

# 가지 길이가 이 값보다 짧아지면 더 이상 갈라지지 않는다.
MIN_LENGTH = 5

# 다음 단계 가지는 현재 가지 길이의 70%로 줄어든다.
REDUCE_RATE = 0.7

# 가지 길이에 비례해 펜 두께를 정하기 위한 비율
WIDTH_RATE = 0.1

# 가지 길이에 곱할 난수 비율의 최솟값과 최댓값
RANDOM_RATE_MIN = 0.9
RANDOM_RATE_MAX = 1.1

def tree(length):
	# 각 가지 길이에 약간의 랜덤 비율을 곱해 매번 조금 다른 길이가 나오게 한다.
	rate = random.uniform(RANDOM_RATE_MIN, RANDOM_RATE_MAX)

	# 실제로 이번 호출에서 사용할 가지 길이
	len = length * rate

	# 길이에 비례해 굵기를 조절하면 굵은 줄기와 가는 가지가 자연스럽게 표현된다.
	t.width(len * WIDTH_RATE)

	# 현재 길이만큼 앞으로 이동하며 줄기 또는 가지를 그린다.
	t.forward(len)

	# 충분히 긴 가지라면 좌우로 다시 갈라지게 한다.
	if len > MIN_LENGTH:
		# 하위 가지는 현재 가지보다 더 짧아진다.
		sub = len * REDUCE_RATE

		# 왼쪽 가지를 그린다.
		t.left(ANGLE)
		tree(sub)

		# 오른쪽 가지를 그리기 위해 반대쪽으로 회전한다.
		t.right(2 * ANGLE)
		tree(sub)

		# 상위 가지의 방향을 유지하기 위해 원래 각도로 되돌린다.
		t.left(ANGLE)

	# 이 호출의 시작 위치로 되돌아가야 상위 줄기에서 다른 가지를 이어 그릴 수 있다.
	t.backward(len)


# 그리는 과정을 빠르게 보기 위해 최고 속도로 설정한다.
t.speed(0)

# 창 제목을 설정한다.
t.title("재귀 호출로 나무 그리기 #2: 랜덤 요소 추가")

# 화면 아래쪽에서 시작해 나무가 위로 자라도록 시작 위치와 방향을 잡는다.
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)

# 길이 120인 줄기에서 시작해 재귀적으로 나무 전체를 그린다.
tree(120)

t.exitonclick()  # 창을 클릭하면 종료
