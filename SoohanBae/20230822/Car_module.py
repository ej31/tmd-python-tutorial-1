# 클래스 정의 (자동차 틀)
class Car:
    def __init__(self, color, model):
        self._color = color
        self._model = model
        self._is_running = False

    def start_engine(self):
        if not self._is_running:
            print(f"{self._color} 색상 {self._model} 모델 자동차의 엔진이 시작되었습니다.")
            self._is_running = True
        else:
            print("이미 엔진이 작동 중입니다.")

    def accelerate(self):
        if self._is_running:
            print(f"{self._color} 색상 {self._model} 모델 자동차가 가속 중입니다.")
        else:
            print("먼저 엔진을 시작하세요.")

    def stop(self):
        if self._is_running:
            print(f"{self._color} 색상 {self._model} 모델 자동차가 정지되었습니다.")
            self._is_running = False
        else:
            print("이미 엔진이 꺼져 있습니다.")
