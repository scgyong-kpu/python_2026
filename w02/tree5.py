"""
재귀 호출로 더 나무답게 보이는 나무를 그리는 예제.

이 버전은 앞선 예제들보다 다음 점을 더 신경 쓴다.
1. 좌우 가지의 길이와 각도를 따로 랜덤화해 대칭을 줄인다.
2. 큰 줄기는 오래 유지하고, 끝부분 가지는 더 빠르게 짧아지게 만든다.
3. 줄기, 잔가지, 잎의 색을 구분하고 같은 계열 안에서도 조금씩 변화시킨다.
4. 잎은 주로 끝부분에 몰아서 배치해 실제 나무 같은 실루엣을 만든다.
5. 시작 위치와 방향을 명확하게 지정해 코드의 의도를 읽기 쉽게 한다.
"""

import random
import turtle

# 나무의 전체 재귀 깊이. 값이 클수록 더 복잡하고 풍성해진다.
MAX_LEVEL = 7

# 첫 줄기의 시작 길이
ROOT_LENGTH = 140

# 잎은 이 단계 이하에서 집중적으로 그린다.
LEAF_LEVEL = 2

# 줄기 굵기를 계산할 때 사용하는 최소값
MIN_WIDTH = 1

# 가지 각도와 길이에 줄 무작위 변화의 범위
COLOR_VARIATION_MIN = 0.85
COLOR_VARIATION_MAX = 1.15

# 색상 기준값
COLOR_LEAF = (70, 150, 45)
COLOR_TWIG = (95, 70, 40)
COLOR_BRANCH = (120, 82, 48)
COLOR_TRUNK = (90, 60, 35)


def clamp_color_value(value):
	# turtle.colormode(255)를 사용하므로 RGB 값은 0~255 범위로 제한한다.
	return max(0, min(255, int(value)))


def vary_color_value(value):
	# 기준 색에 약간의 무작위 변화를 더해 모든 가지와 잎이 조금씩 다르게 보이게 한다.
	return clamp_color_value(value * random.uniform(COLOR_VARIATION_MIN, COLOR_VARIATION_MAX))


def color_near(color):
	# 기준 색 주변의 비슷한 색을 만들어 자연스러운 변화를 준다.
	r, g, b = color
	return (
		vary_color_value(r),
		vary_color_value(g),
		vary_color_value(b),
	)


def set_branch_color(level, width):
	# 굵고 높은 단계는 줄기색, 얇은 끝부분은 잎색에 가까운 색을 사용한다.
	if level <= LEAF_LEVEL or width < 1.4:
		base_color = COLOR_LEAF
	elif width < 3.0:
		base_color = COLOR_TWIG
	elif level >= MAX_LEVEL - 1:
		base_color = COLOR_TRUNK
	else:
		base_color = COLOR_BRANCH
	turtle.color(color_near(base_color))


def branch_width(level):
	# 선형 감소보다 약간 더 자연스럽게 보이도록 지수 형태로 굵기를 줄인다.
	return max(MIN_WIDTH, 0.9 * (level ** 1.35))


def child_length_range(level):
	# 큰 줄기는 비교적 길게 유지하고, 끝부분 가지는 더 급격히 짧아지게 만든다.
	if level >= 6:
		return (0.74, 0.84)
	if level >= 4:
		return (0.64, 0.76)
		
	return (0.52, 0.68)


def pick_branch_count(level):
	# 굵은 줄기에서는 두 갈래가 많고, 중간 이하에서는 세 갈래가 섞이도록 한다.
	if level >= 6:
		return 2
	if level >= 4:
		return random.choices([2, 3], weights=[7, 3])[0]
	return random.choices([2, 3], weights=[5, 5])[0]


def pick_relative_angles(level, branch_count):
	# 모든 가지를 완전히 대칭으로 두지 않고, 위를 향한 상태에서 조금씩 다른 각도로 퍼지게 한다.
	if branch_count == 2:
		return [
			random.uniform(18, 34),
			-random.uniform(14, 28),
		]

	center_bias = random.uniform(-6, 8) if level <= 4 else random.uniform(-4, 6)
	return [
		random.uniform(24, 38),
		center_bias,
		-random.uniform(20, 34),
	]


def draw_leaf():
	# 잎사귀 하나를 작은 곡선 두 개로 그려 끝부분이 부드럽게 보이게 한다.
	size = random.uniform(7, 13)
	turtle.width(1)
	turtle.begin_fill()
	turtle.right(35)
	turtle.circle(size, 75)
	turtle.left(110)
	turtle.circle(size, 75)
	turtle.left(175)
	turtle.end_fill()


def draw_leaf_cluster(level):
	# 가지 끝부분에 잎 여러 장을 모아 그려 나무 실루엣이 풍성하게 보이게 한다.
	leaf_count = random.randint(3, 6) if level <= 1 else random.randint(2, 4)
	base_heading = turtle.heading()
	base_position = turtle.pos()

	for _ in range(leaf_count):
		turtle.penup()
		turtle.goto(base_position)
		turtle.setheading(base_heading + random.uniform(-45, 45))
		turtle.forward(random.uniform(0, 10))
		set_branch_color(1, 0.8)
		turtle.pendown()
		draw_leaf()

	turtle.penup()
	turtle.goto(base_position)
	turtle.setheading(base_heading)


def draw_tree(level, length, sprig_only=False):
	# 현재 단계에 맞는 길이, 굵기, 색을 정하고 줄기를 그린다.
	width = branch_width(level)
	set_branch_color(level, width)

	if sprig_only:
		draw_leaf_cluster(level)
		return

	turtle.width(width)
	turtle.pendown()
	turtle.forward(length)

	# 끝부분에 가까워지면 줄기 대신 잎 무리를 집중적으로 그린다.
	if level <= LEAF_LEVEL:
		draw_leaf_cluster(level)
	else:
		branch_count = pick_branch_count(level)
		parent_heading = turtle.heading()
		relative_angles = pick_relative_angles(level, branch_count)
		child_min, child_max = child_length_range(level)

		# 각 하위 가지는 각도와 길이를 따로 정해서 대칭적이지 않게 만든다.
		for relative_angle in relative_angles:
			child_length = length * random.uniform(child_min, child_max)
			turtle.setheading(parent_heading + relative_angle)
			draw_tree(level - 1, child_length)

		# 자식 가지를 모두 그린 뒤 원래 방향으로 복구한다.
		turtle.setheading(parent_heading)

		# 중간 끝부분에도 드물게 작은 잎 무리를 더해 풍성함을 만든다.
		if 3 <= level <= 4 and random.random() < 0.18:
			draw_leaf_cluster(level)

	# 상위 가지에서 다른 분기를 이어 그릴 수 있도록 현재 줄기 시작점으로 되돌아간다.
	turtle.penup()
	turtle.backward(length)


# 그리는 과정을 빠르게 보기 위해 최고 속도로 설정한다.
turtle.speed(0)

# 창 제목을 설정한다.
turtle.title("나무 그리기 #5: 더 자연스러운 나무")

# RGB 0~255 범위의 색상을 사용하도록 색상 모드를 바꾼다.
turtle.colormode(255)

# 화면 아래쪽 중앙에서 시작해 위로 자라는 나무처럼 보이게 배치한다.
turtle.penup()
turtle.goto(0, -300)
turtle.setheading(90)
turtle.pendown()

# 첫 줄기에서 시작해 재귀적으로 나무 전체를 그린다.
draw_tree(MAX_LEVEL, ROOT_LENGTH)

turtle.exitonclick()  # 창을 클릭하면 종료
