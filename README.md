# lecture_4

# 클래스 정의하고 객체를 만드는 방법

가장 기본은 keyword로 class를 사용해서 정의 한다.

```python
#obj_1.py
class Cat:
    pass

raon = Cat()
print(raon)
```





인스턴스 메서드를 만드는 가장 기본적인 방법은 다음과 같다(self 를 추가 )

```python
class Cat:
    #class variable or member
    color = 'red'
    #instance method
    def meow(self):
        print('야옹~ 야옹~!')
        

```





class 를 만들고 이를 객체로 활용하기 위해서는  생성자가 필요하다.

그러므로 생성자 만들어 줘야 한다.(`__init__` 를 이용하여 만들어 준다.)

```python

```
