import turtle

# 거북이 객체 생성 및 그리기 속성 설정
t = turtle.Turtle()
t.speed(0)   # 가장 빠른 속도로 설정
t.pensize(4) # 펜 두께를 4로 설정

# 시작점으로 이동
t.penup()
t.backward(400) # 시작점을 왼쪽으로 당겨 본다. 문제 없이 그려질 것이다.
t.left(90)
t.forward(100)
t.right(90)  # 방향 0° (오른쪽)

t.left(20)  # 방향 20° (오른쪽 위). 
# 이렇게 방향을 바꿔서 그려도 문제 없다. 방향이 바뀌어도 그릴 수 있는 도형은 여전히 그릴 수 있다.
# 프로그램을 잘 작성하려면, 요구사항 변경에 유연하게 대응할 수 있도록 작성하는 것이 좋다.
# 어떤 요구사항이 변경될 수 있을지 감을 잡고 이에 대비하여 프로그래밍 하는 습관을 기른다.
# 이것은 프로그래밍 경험을 쌓으면서 점점 더 잘하게 될 것이다.

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
