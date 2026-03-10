"""
한글 자모를 거북이 그래픽으로 그리기 위한 보조 모듈.

이 모듈의 핵심 아이디어는 "현재 위치를 한 글자의 기준점"으로 삼는 것이다.
각 자모 함수는 기준점에서 필요한 획을 그린 뒤, 다시 원래 기준점으로 돌아온다.
이렇게 하면 호출하는 쪽에서는 복잡한 좌표 계산을 하지 않고도
초성, 중성, 종성을 순서대로 조합해 글자를 만들 수 있다.

`scale`은 글자 크기의 기준 길이이고,
`draw_final()`은 받침을 그리고 나서 다음 글자의 시작 위치로 이동시키는 역할을 한다.
"""

import turtle as t

scale = 100

def move_to(x, y):
	"""펜을 들고 지정한 좌표로 이동한 뒤 다시 펜을 내린다."""
	t.penup()
	t.goto(x, y)
	t.pendown()

def draw_kiyeok(xs = 1):
	"""현재 기준점에서 초성/종성 'ㄱ' 모양을 그린다."""
	x,y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(100)
	t.forward(scale / 2)
	move_to(x, y)

def draw_mieum(xs = 1):
	"""현재 기준점에서 받침이나 자음으로 쓸 'ㅁ' 모양을 그린다."""
	x, y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(90)
	t.forward(scale / 2)
	t.right(90)
	t.forward(scale * xs)
	t.right(90)
	t.forward(scale / 2)
	move_to(x, y)

def draw_ieung(xs = 1):
	"""현재 기준점을 기준으로 원형 자음 'ㅇ'을 그린다."""
	x, y = t.pos()
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.setheading(0)
	t.circle(scale * 0.4)
	move_to(x, y)
    
def draw_yo():
	"""현재 기준점 아래쪽에 모음 'ㅛ'를 그린다."""
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.6)
	t.left(90)
	t.forward(scale * 0.2)
	move_to(x + scale * 0.6, y2)
	t.forward(scale * 0.2)
	move_to(x, y)

def draw_i():
	"""현재 기준점의 오른쪽에 세로 모음 'ㅣ'를 그린다."""
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	move_to(x, y)

def draw_final(func = None):
	"""
	받침을 그린 뒤 다음 글자의 시작 위치로 이동한다.

	`func`가 주어지면 현재 글자의 아래쪽에 받침을 그리고,
	없으면 받침 없이 바로 다음 글자 위치로 이동한다.
	"""
	x, y = t.pos()
	if func != None:
		move_to(x, y - scale * 1.5)
		func()
	move_to(x + scale * 2, y)

