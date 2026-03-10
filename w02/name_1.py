import turtle

# 거북이 객체 생성 및 그리기 속성 설정
t = turtle.Turtle()
t.speed(0)   # 가장 빠른 속도로 설정
t.pensize(4) # 펜 두께를 4로 설정

# 성 '김'의 첫 글자 'ㄱ' 그리기

# 시작 위치로 이동한 뒤 'ㄱ' 모양을 그린다.
t.penup()
t.goto(-300, 100)
t.pendown()
t.goto(-270, 100)
t.goto(-270, 60)

# 오른쪽에 세로획 'ㅣ'를 그린다.
t.penup()
t.goto(-255, 100)
t.pendown()
t.goto(-255, 60)

# 아래쪽에 네모 모양 'ㅁ'을 그린다.
t.penup()
t.goto(-295, 45)
t.pendown()
t.goto(-260, 45)
t.goto(-260, 10)
t.goto(-295, 10)
t.goto(-295, 45)

# 이름의 두 번째 글자 '기'를 그린다.

# 왼쪽에 'ㄱ' 모양을 그린다.
t.penup()
t.goto(-210, 100)
t.pendown()
t.goto(-170, 100)
t.goto(-170, 50)

# 오른쪽에 세로획 'ㅣ'를 그린다.
t.penup()
t.goto(-155, 100)
t.pendown()
t.goto(-155, 10)


# 이름의 세 번째 글자 '용'을 그린다.

# 위쪽에 초성 'ㅇ'을 그린다.
t.penup()
t.goto(-55, 80)
t.pendown()
t.circle(15)

# 가운데에 모음 'ㅛ'를 그린다.
# 왼쪽 세로선을 그린다.
t.penup()
t.goto(-70, 73)
t.pendown()
t.goto(-70, 50)

# 오른쪽 세로선을 그린다.
t.penup()
t.goto(-40, 73)
t.pendown()
t.goto(-40, 50)

# 아래 가로선을 그린다.
t.penup()
t.goto(-75, 50)
t.pendown()
t.goto(-35, 50)

# 아래쪽에 받침 'ㅇ'을 그린다.
t.penup()
t.goto(-55, 10)
t.pendown()
t.circle(15)

turtle.exitonclick()  # 창을 클릭하면 종료

