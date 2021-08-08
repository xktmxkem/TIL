# OOP(Object Oriented Programming)

* 객체(Object)

* 객체지향프로그래밍(Object Oriented Programming)

* 클래스(Class)와 객체(Object)

  ![0727_2](../python_asset/0727_2.png)

> #  객체
>
> * Python에서 **모든 것은 객체(object)**입니다.
>
>   모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가집니다.
>
>   - **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가?
>   - **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
>   - **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?
>
> > ### 1.1 타입(Type)과 인스턴스(Instance)
> >
> > |   type |                 instance |
> > | -----: | -----------------------: |
> > |  `int` |            `0`, `1`, `2` |
> > |  `str` | `''`, `'hello'`, `'123'` |
> > | `list` |       `[]`, `['a', 'b']` |
> > | `dict` | `{}`, `{'key': 'value'}` |
> >
> > > 1.1.1 **` 타입(Type)`**
> > >
> > > * 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류
> > >
> > > 1.1.2 **`인스턴스(Instance)`**
> > >
> > > * 특정 타입(type)의 실제 데이터 예시(instance)입니다.
> > > * 파이썬에서 모든 것은 객체이고, **모든 객체는 특정 타입의 인스턴스**입니다.
> >
> > ## 1.2 속성(Attribute)과 메서드(Method)
> >
> > 객체의 속성(상태, 데이터)과 조작법(함수)을 명확히 구분해 봅시다.
> >
> > |      type |       attributes |                                methods |
> > | --------: | ---------------: | -------------------------------------: |
> > | `complex` | `.real`, `.imag` |                                        |
> > |     `str` |                _ | `.capitalize()`, `.join()`, `.split()` |
> > |    `list` |                _ |   `.append()`, `.reverse()`, `.sort()` |
> > |    `dict` |                _ |     `.keys()`, `.values()`, `.items()` |
> >
> > > 1.2.1 **`속성(Attribute)`**
> > >
> > > * 속성(attribute)은 객체(object)의 상태/데이터를 뜻합니다.
> > >
> > > * ```py
> > >   <객체>.<속성>
> > >   ```
> > >
> > > 1.2.2 **`메서드(Method)`**
> > >
> > > * 특정 객체에 적용할 수 있는 행위(behavior)를 뜻 합니다.
> > >
> > > * ```py
> > >   <객체>.<메서드>()
> > >   ```
>
> # 객체 지향 프로그래밍(Object-Oriented Programming)
>
> * Object가 중심(oriented)이 되는 프로그래밍
>
> * 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나입니다.
>
>   객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것입니다.
>
> > ### 2.1 절차 중심 vs. Object 중심
> >
> > * 프로그래밍 패러다임: 어떻게 프로그램을 작성할 것인가
> >
> > ### 2.2  Object 중심의 장점
> >
> > - 코드의 **직관성**
> >
> > - 활용의 **용이성**
> >
> > - 변경의 **유연성**
> >
> > - 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됩니다.
> >
> >   또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며,
> >
> >   보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있습니다.
>
> # 클래스(Class)와 인스턴스(Instance)
>
> * `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드
>
> * `instance`: 객체의 실체와 예, 인스턴스(instance)를 활용
>
> >### 3.1 `클래스(Class) 생성`
> >
> >* 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능합니다.
> >* `<클래스의 이름>`은 `PascalCase`로 정의합니다.
> >* 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 데이터는 **속성(attribute)** 정의된 함수는 **메서드(method)**로 부릅니다.
> >
> >```python
> >class <클래스이름>:
> >    <statement>
> >class ClassName:
> >    statement
> >```
> >
> >
> >
> >### 3.2 `filter(function, iterable)`
> >
> >* iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환합니다.
> >
> >- `filter object` 를 반환합니다.
> >
> >### 3.3 `zip(*iterables)`
> >
> >* 복수의 iterable 객체를 모아(`zip()`)준다.
> >
> >- 결과는 튜플의 모음으로 구성된 `zip object` 를 반환한다.
> >
> >---

https://myjamong.tistory.com/274

