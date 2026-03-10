"""
재귀 호출로 나무를 그리되, 단계(level), 가지 개수, 색상, 잎사귀 모양까지 활용해
더 풍부한 형태의 나무를 만드는 예제.

앞선 예제들이 "두 갈래로 반복 분기하는 나무"를 중심으로 했다면,
이 파일은 다음 요소를 추가해 더 실제 나무에 가까운 느낌을 만든다.
1. 재귀 단계에 따라 줄기 길이와 굵기가 달라진다.
2. 단계에 따라 줄기색과 잎색이 달라진다.
3. 가지 수가 항상 같지 않고 2개 또는 3개로 달라진다.
4. 가장 끝에서는 단순 선 대신 잎사귀 모양을 직접 그린다.
5. 중간 가지에서도 작은 잎 무리를 추가해 더 풍성하게 만든다.
"""

import turtle
import random

# 나무의 전체 재귀 깊이. 값이 클수록 더 복잡하고 풍성한 나무가 만들어진다.
MAX_LEVEL = 7

def adjustColorValue(v):
	# 색상값에 약간의 난수를 주어 같은 계열 안에서도 조금씩 다른 색을 만든다.
	v = int(v * random.uniform(0.8, 1.2))
	if v > 255: v = 255
	return v

def setColor(level):
	# level이 작을수록 나무의 끝부분이므로 초록색 계열을 사용한다.
	# level이 클수록 줄기 쪽이므로 갈색 계열을 사용한다.
	if level <= 2:
		(r, g, b) = (80, 255 - level * 30, 80)
	else:
		# 줄기 쪽으로 갈수록 더 어둡고 갈색에 가까운 색을 쓴다.
		bright = level - 2
		(r, g, b) = (180 - 20 * level, 120 - 10 * level, 80 - 8 * level)

	# 기준 색상에 약간의 무작위 변화를 더한다.
	r = adjustColorValue(r)
	g = adjustColorValue(g)
	b = adjustColorValue(b)

	turtle.color((r, g, b))

def leaf():
	# 나무 끝에 그릴 잎사귀 하나를 타원형 비슷한 모양으로 그린다.
	size = random.uniform(10, 15)
	turtle.width(1)
	turtle.right(45)
	turtle.begin_fill()
	turtle.circle(size, 90)
	turtle.left(90)
	turtle.circle(size, 90)
	turtle.end_fill()
	turtle.left(135)

def tree(level, leavesOnly = False):
	# level 값에 따라 현재 줄기 길이를 정한다.
	# 같은 단계라도 길이가 조금씩 달라지도록 난수를 섞는다.
	length = level * random.uniform(17, 23)

	# 현재 단계에 맞는 색상을 선택한다.
	setColor(level)

	# 가장 끝 단계(level == 1)에서는 더 이상 줄기를 그리지 않고 잎사귀를 그린다.
	if level == 1:
		leaf()
		# turtle.left(180)
		# turtle.stamp()
		# turtle.right(180)
	# leavesOnly가 False인 일반 경우에만 줄기나 가지를 그린다.
	elif not leavesOnly:
		# 단계가 높을수록 더 굵은 줄기를 사용한다.
		turtle.width(level * 3 - 2)
		turtle.pendown()
		turtle.forward(length)

	# 아직 끝 단계가 아니라면 하위 가지를 재귀적으로 만든다.
	if (level > 1):
		# 가지 수를 2개 또는 3개로 정해 더 다양한 모양을 만든다.
		branchCount = random.randint(2, 3)
		step = 60 / branchCount
		# 첫 가지를 그리기 전에 약간 한쪽으로 기울인다.
		angle = random.uniform(-25, -15)
		turtle.right(angle)
		for _ in range(branchCount):
			# 현재 위치에서 한 단계 작은 가지를 그린다.
			tree(level - 1)
			# 다음 가지를 그릴 수 있도록 방향을 조금씩 바꾼다.
			a = (40.0 / (branchCount - 1)) * random.uniform(0.9, 1.1)
			turtle.right(a)
			angle += a
		# 하위 가지들을 모두 그린 뒤 원래 방향으로 복구한다.
		turtle.left(angle)

	# 실제 줄기를 그린 경우에는 원래 위치로 되돌아가 상위 호출의 다른 가지를 이어 그릴 수 있게 한다.
	if level != 1 and not leavesOnly:
		turtle.penup()
		turtle.backward(length)

	# 중간 가지 주변에 작은 잎 무리를 추가해 나무가 더 풍성하게 보이도록 한다.
	if level in range(3, 7) and random.random() < 0.3:
		tree(2, True)


# 그리는 과정을 빠르게 보기 위해 최고 속도로 설정한다.
turtle.speed(0)
# 창 제목을 설정한다.
turtle.title("나무 그리기 #4: 새로운 형태의 나무")


# 화면 아래쪽에서 시작해 위로 자라는 나무처럼 보이도록 시작 위치를 잡는다.
turtle.penup()
turtle.left(90)
turtle.backward(300)
turtle.pendown()

# RGB 0~255 범위의 색상을 사용하도록 색상 모드를 바꾼다.
turtle.colormode(255)

# 최대 단계에서 시작해 전체 나무를 그린다.
tree(MAX_LEVEL)

turtle.exitonclick()  # 창을 클릭하면 종료
