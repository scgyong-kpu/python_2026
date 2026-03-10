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

turtle.exitonclick()  # 창을 클릭하면 종료

