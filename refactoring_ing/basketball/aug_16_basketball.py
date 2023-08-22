# 기본 클래스

class Player:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def offence(self):
        print(f"24초 내에 공격합니다.")

    def defence(self):
        print(f"상대팀의 공격을 막습니다.")

    def classification(self):   # 키에 따라 포지션을 분류합니다.
        if self.height < 190:   # 190보다 작으면 가드
            print(f"{self.name} 선수는 가드입니다.")

        elif 190 <= self.height < 200:    # 190 ~ 200 사이면 포워드
            print(f"{self.name} 선수는 포워드입니다.")

        elif self.height >= 200:    # 200보다 크면 센터
            print(f"{self.name} 선수는 센터입니다.")


class Guard(Player):
    def __init__(self, name, height, speed):
        super().__init__(name, height)    # Player 클래스에서 상속받습니다.
        self.speed = speed


    def dribbling(self):
        print(f"{self.name}선수가 {self.speed}의 속도로 드리블합니다.")

    def three_points_shoot(self):
        print(f"{self.name} 선수가 3점슛을 성공시킵니다.")

    def assist(self):
        print(f"{self.name} 선수의 환상적인 패스입니다.")


class Forward(Player):
    def __init__(self, name, height, jump_ability):
        super().__init__(name, height)      # Player 클래스로부터 상속받습니다.
        self.jump_ability = jump_ability


    def middle_shoot(self):
        print(f"{self.name} 선수가 미들슛을 성공 시킵니다.")

    def rebound(self):
        print(f"{self.name} 선수가 {self.jump_ability}의 점프로 리바운드를 따냅니다.")

    def block_shoot(self):
        print(f"{self.name} 선수가 {self.jump_ability}의 점프로 상대선수의 슛을 블락합니다.")


class Center(Player):
    def __init__(self, name, height, power):
        super().__init__(name, height)
        self.power = power


    def rebound(self):
        print(f"{self.name} 선수가 {self.power}의 힘으로 리바운드를 따냅니다.")

    def block_shoot(self):
        print(f"{self.name} 선수가 {self.power}의 파워로 상대선수의 슛을 블락합니다.")

    def dunk(self):
        print(f"{self.name} 선수가 덩크슛을 내리 꽃습니다. 백보드가 깨졌습니다.")


# heo_hun = Player("허훈", 180)
# heo_hun.classification()
#
# heo_ung = Guard("허웅", 183, 30)
# heo_ung.assist()
# heo_ung.dribbling()
# heo_ung.three_points_shoot()
#
# moon_sunggon = Forward("문성곤", 196, 50)
# moon_sunggon.rebound()
# moon_sunggon.block_shoot()
#
# ra_guna = Center("라건아", 200, 500)
# ra_guna.dunk()