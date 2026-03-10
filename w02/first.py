import turtle as t  # turtle 그래픽 모듈 불러오기. turtle 모듈을 t라는 이름으로 사용

# 정사각형 그리기 (각 변의 길이: 100)
t.forward(100)   # 앞으로 100 이동
t.right(90)      # 오른쪽으로 90도 회전
t.forward(100)   # 앞으로 100 이동
t.right(90)      # 오른쪽으로 90도 회전
t.forward(100)   # 앞으로 100 이동
t.right(90)      # 오른쪽으로 90도 회전
t.forward(100)   # 앞으로 100 이동 (마지막 변)

# 별 그리기 (각 변의 길이: 100, 회전 각도: 144도)
t.forward(100)   # 앞으로 100 이동
t.right(144)     # 오른쪽으로 144도 회전
t.forward(100)   # 앞으로 100 이동
t.right(144)     # 오른쪽으로 144도 회전
t.forward(100)   # 앞으로 100 이동
t.right(144)     # 오른쪽으로 144도 회전
t.forward(100)   # 앞으로 100 이동
t.right(144)     # 오른쪽으로 144도 회전
t.forward(100)   # 앞으로 100 이동 (마지막 변)

# t.done()  # turtle 그래픽 종료. 창이 닫히지 않도록 함.
t.exitonclick()  # 창을 클릭하면 종료