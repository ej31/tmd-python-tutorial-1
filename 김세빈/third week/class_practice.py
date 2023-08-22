'''
컴포지션 - 한 클래스가 다른 클래스의 인스턴스를 포함
'''
class Engine:
    def start(self):
        print("Engine Start")

class Window:
    def up(self):
        print("창문이 올라갑니다")
    def down(self):
        print("창문이 내려갑니다")

class Car:
    def __init__(self):
        self.engine = Engine() # has - a 형태
        self.window = Window()
# 상속보다는 컴포지션을 좀더 추천함!
