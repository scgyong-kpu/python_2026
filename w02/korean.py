"""
한글 문자열을 거북이 그래픽으로 그리기 위한 보조 모듈.

이 모듈은 자음과 모음을 그리는 함수들을 따로 준비한 뒤,
완성형 한글 음절을 초성, 중성, 종성으로 분해해서 해당 함수를 차례대로 호출한다.

한글의 완성형 음절은 기본적으로 초성 19개, 중성 21개, 종성 28개의 조합으로 표현된다.
예를 들어 `김`은 초성 `ㄱ`, 중성 `ㅣ`, 종성 `ㅁ`으로 이루어져 있고,
이 모듈은 바로 그 순서대로 함수를 호출해 글자를 그린다.

핵심 아이디어는 현재 거북이 위치를 "한 글자의 기준점"으로 사용하는 것이다.
각 자모 함수는 자기 모양을 그린 뒤 다시 기준점으로 돌아오므로,
호출하는 쪽에서는 복잡한 좌표 계산 없이도 글자를 조합해서 이어 그릴 수 있다.
"""

import turtle as t

# 글자의 크기를 조절하는 기준 길이
scale = 100

def move_to(x, y):
	"""펜을 들고 원하는 좌표로 이동한 뒤 다시 펜을 내려 다음 획을 준비한다."""
	t.penup()
	t.goto(x, y)
	t.pendown()

# 자음 그리기 함수들
# 자음 'ㄱ'을 그리는 함수
def draw_kiyeok(xs = 1):
	x,y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(100)
	t.forward(scale / 2)
	move_to(x, y)

# 자음 'ㄴ'을 그리는 함수
def draw_nieun(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(270)
	t.forward(scale / 2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

# 자음 'ㄷ'을 그리는 함수
def draw_digeut(xs = 1):
	x, y = t.pos()
	t.setheading(180)
	t.penup()
	t.backward(scale * xs)
	t.pendown()
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale / 2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

# 자음 'ㄹ'을 그리는 함수
def draw_rieul(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(90)
	t.forward(scale / 3)
	t.right(90)
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale / 3)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

# 자음 'ㅁ'을 그리는 함수
def draw_mieum(xs = 1):
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

# 자음 'ㅂ'을 그리는 함수
def draw_bieup(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(270)
	t.forward(scale * 0.6)
	t.left(90)
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale * 0.6)
	t.backward(scale * 0.2)
	t.left(90)
	t.forward(scale * xs)
	move_to(x, y)

# 자음 'ㅅ'을 그리는 함수
def draw_siot(xs = 1):
	x, y = t.pos()
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs / 2, y)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

# 자음 'ㅇ'을 그리는 함수
def draw_ieung(xs = 1):
	x, y = t.pos()
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.setheading(0)
	t.circle(scale * 0.4)
	move_to(x, y)

# 자음 'ㅈ'을 그리는 함수
def draw_jieut(xs = 1):
	x, y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs * 0.5, y)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

# 자음 'ㅊ'을 그리는 함수
def draw_chieut(xs = 1):
	x, y = t.pos()
	y1 = y - scale * 0.2
	move_to(x, y1)
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	y2 = y - scale * 0.6
	move_to(x, y2)
	t.goto(x + scale * xs * 0.5, y1)
	t.setheading(90)
	t.forward(scale * 0.2)
	t.backward(scale * 0.2)
	t.goto(x + scale * xs, y2)
	move_to(x, y)

# 자음 'ㅋ'을 그리는 함수
def draw_kieuk(xs = 1):
	x,y = t.pos()
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	t.right(100)
	t.forward(scale / 2)
	t.penup()
	t.backward(scale / 4)
	t.pendown()
	_, y2 = t.pos()
	t.setheading(180)
	t.goto(x, y2)
	move_to(x, y)

# 자음 'ㅌ'을 그리는 함수
def draw_tieut(xs = 1):
	x, y = t.pos()
	t.setheading(180)
	t.penup()
	t.backward(scale * xs)
	t.pendown()
	t.forward(scale * xs)
	t.left(90)
	t.forward(scale * 0.6)
	t.left(90)
	t.forward(scale * xs)
	y2 = y - scale * 0.3
	move_to(x, y2)
	t.forward(scale * xs)
	move_to(x, y)

# 자음 'ㅍ'을 그리는 함수
def draw_pieup(xs = 1):
	x, y = t.pos()
	x1 = x + scale * xs * 0.3
	x2 = x + scale * xs * 0.7
	y2 = y - scale * 0.6
	t.pendown()
	t.setheading(0)
	t.forward(scale * xs)
	move_to(x, y2)
	t.forward(scale * xs)
	move_to(x1, y)
	t.goto(x1, y2)
	move_to(x2, y)
	t.goto(x2, y2)
	move_to(x, y)

# 자음 'ㅎ'을 그리는 함수
def draw_hieut(xs = 1):
	x, y = t.pos()
	t.penup()
	t.setheading(0)
	t.forward(scale * xs * 0.4)
	t.pendown()
	t.forward(scale * xs * 0.2)
	move_to(x + scale * xs * 0.2, y - scale * 0.1)
	t.forward(scale * xs * 0.6)
	move_to(x + scale * xs * 0.5, y - scale * 0.8)
	t.circle(scale * 0.3)
	move_to(x, y)

# 쌍자음이나 겹받침을 공통 방식으로 그리는 함수
def draw_double(cons1, cons2):
	"""쌍자음이나 겹받침처럼 자음 두 개를 나란히 그린다."""
	x, y = t.pos()
	cons1(0.5)
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.6)
	cons2(0.5)
	move_to(x, y)

# 자음 'ㄲ'을 그리는 함수
def draw_dbl_kiyeok():
	draw_double(draw_kiyeok, draw_kiyeok)

# 자음 'ㄸ'을 그리는 함수
def draw_dbl_digeut():
	draw_double(draw_digeut, draw_digeut)

# 자음 'ㅃ'을 그리는 함수
def draw_dbl_bieup():
	draw_double(draw_bieup, draw_bieup)

# 자음 'ㅆ'을 그리는 함수
def draw_dbl_siot():
	draw_double(draw_siot, draw_siot)

# 자음 'ㅉ'을 그리는 함수
def draw_dbl_jieut():
	draw_double(draw_jieut, draw_jieut)

# 겹받침 'ㄳ'을 그리는 함수
def draw_kiyeok_siot():
	draw_double(draw_kiyeok, draw_siot)

# 겹받침 'ㄵ'을 그리는 함수
def draw_nieun_jieut():
	draw_double(draw_nieun, draw_jieut)

# 겹받침 'ㄶ'을 그리는 함수
def draw_nieun_hieot():
	draw_double(draw_nieun, draw_hieut)

# 겹받침 'ㄺ'을 그리는 함수
def draw_rieul_kiyeok():
	draw_double(draw_rieul, draw_kiyeok)

# 겹받침 'ㄻ'을 그리는 함수
def draw_rieul_mieum():
	draw_double(draw_rieul, draw_mieum)

# 겹받침 'ㄼ'을 그리는 함수
def draw_rieul_bieup():
	draw_double(draw_rieul, draw_bieup)

# 겹받침 'ㄽ'을 그리는 함수
def draw_rieul_siot():
	draw_double(draw_rieul, draw_siot)

# 겹받침 'ㄾ'을 그리는 함수
def draw_rieul_tieut():
	draw_double(draw_rieul, draw_tieut)

# 겹받침 'ㄿ'을 그리는 함수
def draw_rieul_pieup():
	draw_double(draw_rieul, draw_pieup)

# 겹받침 'ㅀ'을 그리는 함수
def draw_rieul_hieut():
	draw_double(draw_rieul, draw_hieut)

# 겹받침 'ㅄ'을 그리는 함수
def draw_bieup_siot():
	draw_double(draw_bieup, draw_siot)

# 모음 그리기 함수들
# 모음 'ㅏ'를 그리는 함수
def draw_a():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(0)
	move_to(x2, y - scale * 0.5)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅑ'를 그리는 함수
def draw_ya():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(0)
	move_to(x2, y - scale * 0.4)
	t.forward(scale * 0.2)
	move_to(x2, y - scale * 0.6)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅓ'를 그리는 함수
def draw_eo():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(180)
	move_to(x2, y - scale * 0.5)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅕ'를 그리는 함수
def draw_yeo():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	t.setheading(180)
	move_to(x2, y - scale * 0.4)
	t.forward(scale * 0.2)
	move_to(x2, y - scale * 0.6)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅗ'를 그리는 함수
def draw_o():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.5)
	t.left(90)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅛ'를 그리는 함수
def draw_yo():
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

# 모음 'ㅜ'를 그리는 함수
def draw_u():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.5)
	t.right(90)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅠ'를 그리는 함수
def draw_yu():
	x, y = t.pos()
	y2 = y - scale * 1.15
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	t.backward(scale * 0.6)
	t.right(90)
	t.forward(scale * 0.2)
	move_to(x + scale * 0.6, y2)
	t.forward(scale * 0.2)
	move_to(x, y)

# 모음 'ㅡ'를 그리는 함수
def draw_eu():
	x, y = t.pos()
	y2 = y - scale * 1.25
	move_to(x, y2)
	t.setheading(0)
	t.forward(scale)
	move_to(x, y)

# 모음 'ㅣ'를 그리는 함수
def draw_i():
	x, y = t.pos()
	x2 = x + scale * 1.5
	move_to(x2, y)
	t.goto(x2, y - scale)
	move_to(x, y)

# 모음 'ㅐ'를 그리는 함수
def draw_ae():
	draw_a()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.2)
	draw_i()

# 모음 'ㅒ'를 그리는 함수
def draw_yae():
	draw_ya()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.2)
	draw_i()

# 모음 'ㅔ'를 그리는 함수
def draw_e():
	draw_eo()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.1)
	draw_i()

# 모음 'ㅖ'를 그리는 함수
def draw_ye():
	draw_yeo()
	t.setheading(0)
	t.penup()
	t.forward(scale * 0.1)
	draw_i()

# 모음 'ㅘ'를 그리는 함수
def draw_wa():
	draw_o()
	draw_a()

# 모음 'ㅙ'를 그리는 함수
def draw_wae():
	draw_o()
	draw_ae()

# 모음 'ㅚ'를 그리는 함수
def draw_oi():
	draw_o()
	draw_i()

# 모음 'ㅝ'를 그리는 함수
def draw_weo():
	draw_u()
	draw_eo()

# 모음 'ㅞ'를 그리는 함수
def draw_we():
	draw_u()
	draw_e()

# 모음 'ㅟ'를 그리는 함수
def draw_wi():
	draw_u()
	draw_i()

# 모음 'ㅢ'를 그리는 함수
def draw_eui():
	draw_eu()
	draw_i()

# 종성을 처리하고 다음 글자 위치로 이동하는 함수
def draw_final(func = None):
	"""
	종성을 그린 뒤 다음 글자의 시작 위치로 이동한다.

	받침이 없으면 바로 다음 글자로 이동하고,
	받침 함수가 주어지면 현재 글자의 아래쪽에 종성을 먼저 그린다.
	"""
	x, y = t.pos()
	if func != None:
		move_to(x, y - scale * 1.5)
		func()
	move_to(x + scale * 2, y)

# 초성 인덱스를 실제 자음 함수에 연결하는 표
chosung = [
	draw_kiyeok, draw_dbl_kiyeok, draw_nieun, draw_digeut, 
	draw_dbl_digeut, draw_rieul, draw_mieum, draw_bieup,
	draw_dbl_bieup, draw_siot, draw_dbl_siot, draw_ieung,
	draw_jieut, draw_dbl_jieut, draw_chieut, draw_kieuk,
	draw_tieut, draw_pieup, draw_hieut
]

# 중성 인덱스를 실제 모음 함수에 연결하는 표
joongsung = [
	draw_a, draw_ae, draw_ya, draw_yae,
	draw_eo, draw_e, draw_yeo, draw_ye,
	draw_o, draw_wa, draw_wae, draw_oi,
	draw_yo, draw_u, draw_weo, draw_we,
	draw_wi, draw_yu, draw_eu, draw_eui,
	draw_i
]

# 종성 인덱스를 실제 받침 함수에 연결하는 표
# 종성은 27종이지만, 인덱스 0은 받침이 없는 경우이므로 None으로 채워 총 28개가 된다.
jongsung = [
	None, draw_kiyeok, draw_dbl_kiyeok, draw_kiyeok_siot,
	draw_nieun, draw_nieun_jieut, draw_nieun_hieot,
	draw_digeut, draw_rieul, 
	draw_rieul_kiyeok, draw_rieul_mieum, draw_rieul_bieup, draw_rieul_siot, 
	draw_rieul_tieut, draw_rieul_pieup, draw_rieul_hieut,
	draw_mieum, draw_bieup, draw_bieup_siot, 
	draw_siot, draw_dbl_siot, draw_ieung, draw_jieut, draw_chieut, 
	draw_kieuk, draw_tieut, draw_pieup, draw_hieut
]

def draw_ustr(str):
	"""
	문자열을 받아 한글이면 음절을 분해해 그리고,
	줄바꿈이면 다음 줄로 이동하며, 그 외 문자는 간격만 띄운다.

	완성형 한글 한 글자는 초성, 중성, 종성 번호의 조합으로 표현되므로,
	유니코드 값을 이용해 세 부분으로 분해한 뒤 대응하는 함수를 차례대로 호출한다.
	"""
	ox,oy = t.pos()
	for ch in str:
		char = ord(ch)
		if char >= 0xAC00 and char <= 0xDCAF:
			# 완성형 한글 코드를 초성, 중성, 종성 순서의 인덱스로 바꾼다.
			order = char - 0xAC00
			cho = order // (21 * 28)
			joong = order % (21 * 28) // 28
			jong = order % 28

			# 분해한 결과에 맞는 자모 함수를 순서대로 호출해 한 글자를 완성한다.
			chosung[cho]()
			joongsung[joong]()
			draw_final(jongsung[jong])
		elif char == 0x0A:
			# 줄바꿈 문자를 만나면 다음 줄의 시작 위치로 이동한다.
			oy -= 3 * scale
			move_to(ox, oy)
		else:
			# 한글이 아닌 문자는 폭만 한 칸 띄우고 넘어간다.
			x,y = t.pos()
			move_to(x + scale, y)