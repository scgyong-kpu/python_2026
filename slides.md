# Class Slides

## 2026-03-17
* Homeworks
  - Help from
    - 친구? 책? YouTube? ChatGPT? Cursor/Claude?
  - 중학생 동생이 2차방정식 문제 어떻게 푸는지 물어본다
    - "카메라로 찍어서 ChatGPT 한테 플어달라고 하면 돼"
  - 도움을 받았다면, 왜 그렇게 되는지도 반드시 물어보고, 이해하도록 하자
    - 이해가 안 되면? 더 질문해서 이해가 될때까지
* 실습 방법
  * In IDLE (or REPL)
  * `.py` 파일을 만들어서 실행
  * 수업 시간에 (혹은 끝난 뒤에라도) 화면에 입력하는 것을 IDLE 에서 따라해 보거나 `.py` 파일을 만들어 실행해보기
  * 과제 제출은 과제에서 요구하는 형식의 파일을 만들어 제출하는 방식 사용
* `turtle.write()`
  * 내가 그릴 필요가 없었나?
  * 컴퓨터는 원래 이런 기능이 있지만 우리는 원리를 배우는 중이다
* print formatting
  * `%-formatting`
  * `str.format()`
  * `f-string`
    * 변수 값을 원하는 형태로 출력하기 좋음
    * ```Python
      name = "Kim"
      age = 20
      
      print(f"My name is {name}")
      print(f"I am {age} years old")
      ```
* value vs variable
    ```Python
    turtle.forward(200)
    ```
    ```Python
    distance = 200
    turtle.forward(distance)
    turtle.left(90)
    distance = 100
    turtle.forward(distance)
    ```
* Data Types
    ```Python
    a = 10
    b = 3.14
    c = "hello"
    d = True
    
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    ```
* TypeError
  * 에러 나는 코드
      ```Python
      age = 20
      print("age = " + age) # ❌ TypeError
      ```
  * `+` 대신 `,` 로 해결
      ```Python
      print("age =", age)
      ```
  * 또는 `f-string` 으로 해결
     ```Python
     print(f"age = {age}")
     ```
  * 다음 프로그램 결과 예상해보고, 문제 해결하기
    ```Python
    s = input('Enter a number:')
    # print(type(s))
    print(s * 5)
    ```
    ```Python
    a = "100"
    b = "20"

    print(a + b)
    print(int(a) + int(b))
    ```
* 진수
  * 2진수? 8진수? 16진수?
    ```Python
    a = 10

    print(bin(a))
    print(oct(a))
    print(hex(a))
    ```
* 변수 값 변경
  * 다음 코드의 결과는?
    ```Python
    x = 10
    y = x
    x = 20
    print(y)
    ```
  * 문장은 순차적으로 실행되며, 대입은 우변의 값을 좌변에 옮기는 일이다
* 오늘 수업 핵심
  1. `변수` : 값을 저장하는 상자
  2. `print()` 로 출력
  3. `type()` 으로 데이터형 확인
  4. `f-string` 형태로 출력

* 실습과제
  * `turtle` 을 사용하여 선 길이, 각도, 횟수, 비율 를 지정하여 여러 모양 그리기
    * 프로그램 초반에 세 변수를 선언하고 다음 값들을 넣은 결과 포함하기 (캡쳐) 이 외에도 재미있는 값들 몇 개 더 실행해 보고 캡쳐 추가
      * ```Python
        length = 200
        angle = 90
        count = 4
        rate = 1.0
        ```
      * ```Python
        length = 123
        angle = 72
        count = 5
        rate = 1.0
        ```
      * ```Python
        length = 200
        angle = 144
        count = 5
        rate = 1.0
        ```
      * ```Python
        length = 200
        angle = 170
        count = 36
        rate = 1.0
        ```
      * ```Python
        length = 10
        angle = 60
        count = 10
        rate = 1.5
        ```
      * ```Python
        length = 200
        angle = 89
        count = 200
        rate = 0.99
        ```
  * 태양으로부터 지구까지 빛이 도달하는 시간 구하기 (?분 ?초)
    * 거리는 1억 4960 km
    * 빛의 속도는 299,792,458 m/s
    * 답이 정수로 `m 분 s 초` 로 출력되어야 한다.
  * sin 그래프 그리기
    * `-𝝿` 부터 `+𝝿` 까지의 `sin` 값을 이용하여 `turtle` 을 사용하여 그리기
    * `scale` 값을 이용하여 좌표에 곱해 사용. `100` 정도의 값이 적당
    * 그래프를 그리기 전 축을 그려 놓고 시작
      * x축은 `-2𝝿` 부터 `+2𝝿` 까지
      * y축은 `-1` 부터 `+1` 까지
    * `math` 모듈 이용
      * `math.sin()` 과 `math.pi` 값 활용
    * `step` 값만큼 `x` 를 이동하며 그리며, 초기값은 `0.1` 로 해 보고 변경해 본다
    * 다음 Loop 구조를 활용한다
      ```Python
      # 시작 위치로 펜 올리고 이동한 뒤 펜 내리기
      
      # 루프를 돌며 선 그리기
      while x <= end_x:
          y = # sin 값 계산
          # 거북이를 x, y 로 이동시키기
          # x 에 step 만큼 더하기

      # 모든 goto 의 x, y 좌표에는 scale 을 곱해서 이동하기
      ```

## 2026-03-10
* Tools
  - Python Interpreter
  - VSCode + Extensions
  - REPL/cmd-CLI/IDLE
  - Sublime Text
* IDLE
  - REPL vs file
  - Calculation
  - turtle
* Module
  - as
  - from - import
* VSCode
  - Extensions
  - Edit, Run, Debug
* Turtle
  - forward/backward, left/right, penup/pendown
  - circle
  - goto
  - Loop, function

* Name
  - name_1: goto
  - name_2: forward/backward
  - kky: function/module
    - jamo: module for kky
  - scgyong: arbitrary Korean characters
    - korean: all consonants/vowels

* Tree
  - V0: simple
    - done / exitonclick
    - speed
  - V1: width
  - V2: random
    - random module
  - V3: color
  - V4: transform

* Book: Chapter 2
  - Variables, Tuple
  - ppt 17: Programming
  - input()
  - ’’’ comment


## 2026-03-03

* 앞으로 채워 앉으세요
* Python
  - 김기용, 게임공학부
* Programming, Why python
* Listen?
* Why, What, How
* Tools:
  - Editor, Interpreter, Debugger, AI Assistant/Agent
* Blockly-Games, Logo, Turtles
  - Tree/Korean
* Procedural, OOP, Functional, Multi-threading
* Online Lecture First
* Read Notices
* Homework Requirements


