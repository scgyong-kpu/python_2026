import turtle as t  # turtle 그래픽 모듈 불러오기. turtle 모듈을 t라는 이름으로 사용

def draw_shape(sides, angle):
    """주어진 변의 수와 회전 각도로 도형을 그리는 함수"""
    for _ in range(sides):
        t.forward(100)  # 앞으로 100 이동
        t.right(angle)   # 오른쪽으로 주어진 각도 회전

draw_shape(4, 90)  # 4개의 변과 90도 회전으로 정사각형 그리기
draw_shape(5, 144) # 5개의 변과 144도 회전으로 별 그리기

# t.done()  # turtle 그래픽 종료. 창이 닫히지 않도록 함.
t.exitonclick()  # 창을 클릭하면 종료