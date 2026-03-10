import turtle

# 거북이 객체 생성 및 그리기 속성 설정
t = turtle.Turtle()
t.speed(0)   # 가장 빠른 속도로 설정
t.pensize(4) # 펜 두께를 4로 설정

# 시작점으로 이동
t.penup()
t.backward(300)
t.left(90)
t.forward(100)
t.right(90)  # 방향 0° (오른쪽)

# 김 

# ㄱ 모양을 그린다.
t.pendown()
t.forward(30)
t.right(130)
t.forward(40)
t.left(170)

# 오른쪽 세로획을 그리기 위해 이동한다.
t.penup()
t.forward(60)
t.right(130)
t.pendown()
t.forward(40)

# 아래쪽 네모 부분을 그린다.
t.penup()
t.forward(10)
t.pendown()
t.forward(20)
t.right(90)
t.forward(40)
t.right(90)
t.forward(20)
t.right(90)
t.forward(40)
t.left(80)
t.penup()
t.forward(44)
t.right(80)

# 기

# 왼쪽 ㄱ 모양을 그린다.
t.pendown()
t.forward(30)
t.right(130)
t.forward(40)
t.left(170)

# 오른쪽 세로획을 그린다.
t.penup()
t.forward(60)
t.right(130)
t.pendown()
t.forward(60)
t.left(170)

# 다음 글자를 그릴 위치로 이동한다.
t.penup()
t.forward(50)
t.right(80)

# 용

# 위쪽 초성 ㅇ을 그릴 위치로 이동한다.
t.forward(30)
t.right(90)
t.forward(20)
t.left(90)

# 초성 ㅇ을 그린다.
t.pendown()
t.circle(13)

# 가운데 모음의 왼쪽 세로획을 그린다.
t.penup()
t.backward(10)
t.right(90)
t.pendown()
t.forward(10)

# 가운데 모음의 오른쪽 세로획을 그린다.
t.penup()
t.backward(10)
t.left(90)
t.forward(20)
t.right(90)
t.pendown()
t.forward(10)

# 가운데 가로획을 그린다.
t.penup()
t.right(90)
t.forward(40)
t.right(180)
t.pendown()
t.forward(60)

# 아래쪽 받침 ㅇ을 그린다.
t.penup()
t.backward(30)
t.right(90)
t.forward(30)
t.left(90)
t.pendown()
t.circle(13)

# 그리기가 끝나면 거북이를 숨긴다.
t.hideturtle()

turtle.exitonclick()  # 창을 클릭하면 종료
