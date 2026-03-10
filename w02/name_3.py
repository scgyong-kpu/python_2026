"""
이 프로그램은 거북이 그래픽을 직접 조작하는 대신, `jamo` 모듈에 준비된
한글 자모 그리기 함수를 조합해서 이름을 그린다.

동작 방식은 다음과 같다.
1. `jamo.move_to(x, y)`로 이름을 쓰기 시작할 기준 위치로 이동한다.
2. 초성, 중성, 종성에 해당하는 함수를 차례대로 호출해 한 글자를 완성한다.
3. `jamo.draw_final()`은 받침을 그린 뒤, 또는 받침이 없더라도 다음 글자를 쓸 수 있게
	기준 위치를 오른쪽으로 옮긴다.
4. 따라서 이 파일은 선을 직접 어디로 그을지 하나하나 계산하기보다,
	"어떤 자모를 어떤 순서로 배치할지"에 집중해서 이름 전체를 구성한다.

아래 코드는 `김기용`을 그리는 예시이다.
- `김`: ㄱ + ㅣ + 받침 ㅁ
- `기`: ㄱ + ㅣ + 받침 없음
- `용`: ㅇ + ㅛ + 받침 ㅇ
"""

import turtle
import jamo

# def move_to(x, y):
#   t.penup()
#   t.goto(x, y)
#   t.pendown()

jamo.move_to(-300, 200)

jamo.draw_kiyeok()
# jamo.draw_dbl_bieup()
jamo.draw_i()
# jamo.draw_final(jamo.draw_kiyeok)
jamo.draw_final(jamo.draw_mieum)

jamo.draw_kiyeok()
jamo.draw_i()
jamo.draw_final()

jamo.draw_ieung()
jamo.draw_yo()
jamo.draw_final(jamo.draw_ieung)

turtle.exitonclick()
