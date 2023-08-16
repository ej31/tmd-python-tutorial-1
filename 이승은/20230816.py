# 20230816 실습
class Player:
    def __init__(self, name, age, position, team, number):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        self.number = number

    def get_name(self):
        return f"name은 {self.name} 입니다."

    def get_age(self):
        return f"age는 {self.age} 입니다."

    def get_position(self):
        return f"position은 {self.position} 입니다."

    def get_team(self):
        return f"team은 {self.team} 입니다."

    def get_number(self):
        return f"number는 {self.number} 입니다."

manny_player = Player("Marcus Rashford", 25, "forward", "Manchester United", "10")
print(manny_player.get_name())
print(manny_player.get_age())
print(manny_player.get_position())
print(manny_player.get_team())
print(manny_player.get_number())