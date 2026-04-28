# Class Slides

## 2026-04-28. 9주차 Homework - Collections

과제 본문에 3번 이상 실행한 것을 텍스트 붙여넣기 하라

1. 숫자 목록 통계 내기 (list)

    * 여러 개의 정수를 입력받아 리스트에 저장한 뒤 다음을 출력하라.

      * 전체 리스트
      * 합계
      * 평균
      * 가장 큰 값
      * 가장 작은 값

    - 실행 방식

      * 숫자를 계속 입력받음
      * 0 이하의 숫자가 입력되면 종료
      * 종료 전에 입력된 값들만 사용

1. 입력된 단어들의 첫 글자별 개수 세기 프로그램
    - 여러 개의 단어를 입력받아, 첫 글자가 같은 단어가 몇 개씩 입력되었는지 세어 출력하는 프로그램을 작성하라.
    - 요구사항
      - `input()`을 이용해 단어를 계속 입력받는다.
      * 빈 문자열을 입력하면 입력을 종료한다.
      * 입력된 각 단어의 첫 글자를 기준으로 개수를 센다.
      * 마지막에 첫 글자별 등장 횟수를 출력한다.
      * 개수 세기에는 `dictionary` 를 사용한다.
    - 참고 사항
      * 단어의 첫 글자는 word[0] 를 이용해 구할 수 있다.
      * 이미 나온 첫 글자라면 개수를 1 증가시킨다.
      * 처음 나온 첫 글자라면 새로 추가하고 값을 1로 저장한다.
      * 입력 종료 후 dictionary의 내용을 반복문으로 출력한다.
      
    - 힌트
  
      * 예를 들어 `apple` 이 입력되면 첫 글자는 `"a"` 이다.
      * `banana` 가 입력되면 첫 글자는 `"b"` 이다.
      * 이 첫 글자를 dictionary의 key로 사용하면 된다.
        ```python
          counts["a"] = 3
          counts["b"] = 2
        ```
  
    - 예시 1
      <pre>
      단어 입력: <b><i>apple</i></b>
      단어 입력: <b><i>banana</i></b>
      단어 입력: <b><i>april</i></b>
      단어 입력: <b><i>blue</i></b>
      단어 입력: <b><i>avocado</i></b>
      단어 입력: <b><i></i></b>
      
      a : 3
      b : 2
      </pre>
  
    - 예시 2
      <pre>
      단어 입력: <b><i>cat</i></b>
      단어 입력: <b><i>car</i></b>
      단어 입력: <b><i>dog</i></b>
      단어 입력: <b><i>desk</i></b>
      단어 입력: <b><i>door</i></b>
      단어 입력: <b><i></i></b>
      
      c : 2
      d : 3
      </pre>

1. 사전 프로그램

    - 영어 단어와 뜻을 저장한 뒤, 단어를 입력하면 뜻을 출력하는 프로그램을 작성하라.
    - 초기 데이터
  
      * apple : 사과
      * banana : 바나나
      * grape : 포도
  
    - 요구사항
  
      * 사전에 없는 단어를 입력하면 "없는 단어입니다" 출력
      * 다음 형식으로 입력되면 사전에 추가
        ```
        @단어 설명
        ```
        - 이를 위해 다음 라인 사용
        - ```python
          import re
          # 정규식 패턴: 
          # ^@(\S+) : @로 시작하고 공백이 아닌 글자들을 그룹1(단어)로 추출
          # \s+(.*) : 그 뒤의 공백을 건너뛰고 나머지 전체를 그룹2(설명)로 추출
          match = re.match(r"^@(\S+)\s+(.*)", line)
          if match:
              word = match.group(1)
              description = match.group(2)
          ```
      * 여러 번 검색 가능
      * `q` 입력 시 종료

## 2026-04-07 

### Loops
* Basic Loop
    ```python
    for i in range(4):
        pass
    ```
* inclusive, exclusive, step
    ```python
    for i in range(10, 20, 2):
        print(f"i = {i}")
    ```
* `for` 안에서 `if` 사용하기
    ```python
    sum = 0
    for i in range(10, 20):
        if i % 2 == 0:
            print(f"i = {i}")
            sum += i
    print(f"sum = {sum}")
    ```
* 중첩된(nested) `for`
    ```python
    for i in range(5):
        for j in range(10):
            print(f"i = {i}, j = {j}")
    ```
* 더 단순한 Loop: `while`, Loop 를 종료시키는 `break`, Loop 의 나머지 부분을 하지 않고 처음으로 돌아가는 `continue`
    ```python
    for i in range(20):
        if i % 4 == 0: continue
        if i == 15: break
        print(f"i = {i}")
    ```

### Homework. 6주차 실습: 반복

프로그램 출력 결과는 3번 이상 실행한 예를 포함시킨다

1. 두 정수를 입력받아 두 수 사이의 합을 구하라. `사이` 에서 양쪽 끝 숫자는 모두 포함한다. 예를 들어 10 과 12 를 입력하면 10+11+12 의 결과인 33 을, 20 과 25 를 입력하면 20+21+22+23+24+25 를 계산한 115 를 출력한다.
    * `input()` 을 이용해 두 숫자를 입력받음
    * 합을 저장할 변수를 초기화
    * `시작값` 부터 `끝값` 까지 Loop 를 돌며 더한다.
    * 결과를 출력한다.

1. 입력받은 숫자만큼의 크기로 별(`*`) 을 이용하여 삼각형을 출력하라.
    * `input()` 을 이용해 하나의 숫자를 입력받음
    * 4를 입력했을 경우 다음과 같이 출력
      ```
      *
      **
      ***
      ****
      ```
    * 7를 입력했을 경우 다음과 같이 출력
      ```
      *
      **
      ***
      ****
      *****
      ******
      *******
      ```
    * (Optional) 왼쪽 아래부분이 직각인 삼각형 말고, 오른쪽 아래가 직각인 삼각형을 만들어 보아도 좋다.

1. 입력받은 숫자들 중 가장 큰 숫자를 출력하는 프로그램
    * 숫자를 입력받는다.
      * 숫자가 0 이하의 수이면 지금까지 입력 받은 숫자들 중 가장 큰 수를 출력하고 종료한다.
      * 그 외의 숫자이면 기억하고 있는 가장 큰 수와 비교하여 더 크면 교체한다
    * 실행 예시는 다음과 같다
      ```
      숫자를 입력하세요: 3
      숫자를 입력하세요: 4
      숫자를 입력하세요: 6
      숫자를 입력하세요: 3
      숫자를 입력하세요: 5
      숫자를 입력하세요: 23
      숫자를 입력하세요: 4
      숫자를 입력하세요: 2
      숫자를 입력하세요: 0
      가장 큰 수는: 23
      ```
      ```
      숫자를 입력하세요: 1
      숫자를 입력하세요: 0
      가장 큰 수는: 1
      ```
      ```
      숫자를 입력하세요: 0
      가장 큰 수는 없습니다
      ```
    * 
## 2026-03-31 

### Homework. 5주차 실습: 조건문

프로그램 출력 결과는 3번 이상 실행한 예를 포함시킨다

1. 점수별 등급 판정
  * 점수를 입력하면 등급을 출력하는 프로그램을 작성한다.
    * `input()` 을 이용해 정수 숫자 하나를 입력받음
    * 입력받은 숫자가
      * 70 미만이면 D등급
      * 70 이상이면 C등급
      * 80 이상이면 B등급
      * 90 이상이면 A등급
      * 100 점이면 S등급
    * 이라고 출력한다.
2. 계산기 확장: 두 숫자와 연산자를 입력받아 연산 결과를 출력한다.
  * `input()` 을 이용해 두 숫자를 입력받음
  * `input()` 을 이용해 문자 하나를 입력받음
  * 입력받은 문자가 다음중 하나이면:
    * `+`, `-`, `*`, `/`, `%` 
  * 해당 계산 결과를 출력. 이때 `3 + 5 = 8` 의 형태로 출력한다
3. 초 를 입력하면 일/시간/분/초 로 변환하여 출력하는 프로그램 (확장)
  * 지난번 과제와 동일
  * 0 인 값은 출력하지 않는다
  * 예:
    * 3607초 의 경우: 1시간 7초
    * 86460초 의 경우: 1일 1분
  * 지난번 과제와 달리, `%02d` 는 사용하지 않는다

## 2026-03-24 

### Slides

* 연산자 우선순위
   * 두뇌풀가동 meme
* 복합 대입연산자
   * = Compound Assignment Operators
* 관계연산자와 논리연산자 결과의 type 은?
   * `bool`
* Bitwise Operators
   * `&`, `|`, `^`, `~`, `<<`, `>>`

### Homework. 4주차 실습: 연산자
1. 가격과 할인율 을 입력하면 할인 금액과 최종 가격을 출력하는 프로그램을 작성한다.
    * `input()` 을 이용해 두 숫자를 입력받음
    * 결과를 두 숫자로 출력
    * 최종 가격은 1원 단위에서 반올림 (435원 ➔ 440원)
    * 예: (***bold italic*** 은 사용자 입력)
     <pre>
     가격: <b><i>10000</i></b>
     할인율: <b><i>20</i></b>
     할인금액: 2000
     최종가격: 8000</pre>

1. 초 를 입력하면 일/시간/분/초 로 변환하여 출력하는 프로그램
    * `input()` 을 이용해 숫자 하나를 입력받음
    * 결과를 다음 포맷으로 숫자로 출력
      * 일 은 숫자만 출력
      * 시간,분,초 는 두 자리로 출력하며 1자리 숫자인 경우 0 으로 채움
    * 예: (***bold italic*** 은 사용자 입력)
     <pre>
     초 입력: <b><i>1000000</i></b>
     결과: 11일 13시간 46분 40초</pre>
     <pre>
     초 입력: <b><i>123123</i></b>
     결과: 1일 10시간 12분 03초</pre>

1. 두 숫자를 입력받아 여러 연산 결과를 모두 출력한다.
   * `input()` 을 이용해 두 숫자를 입력받음
   * `+`, `-`, `*`, `/`, `//`, `%` 결과 출력
   * `/` 의 경우 소수 2째자리까지만 출력
   *  예: (***bold italic*** 은 사용자 입력)
      <pre>
      첫번째 값: <b><i>5</i></b>
      두번째 값: <b><i>3</i></b>
      5 + 3 = 8
      5 - 3 = 2
      5 * 3 = 15
      5 / 3 = 1.66
      5 // 3 = 1
      5 % 3 = 2</pre>


### Homework. 5주차 조사: 조건문
다음 항목들에 대해 조사하라.
* 각 항목의 설명, 언제 사용하는지, 흐름 차이, 예시 코드
  * `if`
  * `if`-`else`
  * `if`-`elif`-`else`
* 중첩된 `if`
* python 에서 `:` 와 들여쓰기 (indent) 의 의미
* Membership (list)
  * `if` ... `in`
  * `if` ... `not in`
* 조건식
  * python 에서 `조건식` 이란?
  * 비교 연산자 (`==`, `!=`, `>`, `<`, `>=`, `<=`) / 논리 연산자 (`and`, `or`, `not`) 와 `if` 의 관계
* `match` - `case` 사용법
* Conditional Expression 사용법
  * 변수 = 참일때값 `if` 조건 `else` 거짓일때값

## 2026-03-17 Homework

* 다음 연산자들의 의미를 정리하라. 의미, 예시코드 등을 사용하라.
  * 산술연산자 `+`, `-`, `*`, `/`, `//`, `%`, `**`
  * 복합대입연산자 `+=`, `-=`, `*=`, `/=`, `%=`
  * 비교 연산자 `==`, `!=`, `>`, `<`, `>=`, `<=`
  * 논리 연산자 `and`, `or`
  * 문자열 연산자
    * 문자열 + 문자열
    * 문자열 * 정수
  * 형변환 연산자
    * `int("100")`, `float("3.14")`, `str(100)`, ...
* 연산자들의 우선순위에 대해 정리하라
* `C` / `C++` / `Java` 등에 있는 `++` 연산자는 Python 에 없다. 왜 없으며, 대안은 무엇인가?

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
    * 거리는 1억 4960만 km
    * 빛의 속도는 299,792,458 m/s
    * 답이 정수로 `m 분 s 초` 로 출력되어야 한다.
  * sin 그래프 그리기
    * `-𝝿` 부터 `+𝝿` 까지의 `sin` 값을 이용하여 `turtle` 을 사용하여 그리기
    * `scale` 값을 이용하여 좌표에 곱해 사용. `100` 정도의 값이 적당
    * 그래프를 그리기 전 축을 그려 놓고 시작
      * x축은 `-𝝿` 부터 `+𝝿` 까지
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


