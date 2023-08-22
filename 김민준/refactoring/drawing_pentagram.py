class PentagramDrawing:

    i = 0
    j = 0
    k = 0
    num_of_space = j
    num_of_letters = k
    max_end_letter_count = num_of_letters + 10
    internalSpace = 0
    s_count = num_of_letters

    @staticmethod
    def draw_upper_part():
        for i in range(1, 21):
            for j in range(1, 71 - i):
                print(" ", end = "")
            for k in range(1, 2 * i + 1):
                print("*", end = "")
            print()

    def draw_upper_middle_part(self):
        while self.num_of_letters > self.max_end_letter_count:
            for i in range(self.num_of_space):
                print(" ", end = "")
            for j in range(self.num_of_letters):
                print("*", end = "")
            print("")

            self.num_of_letters -= 10
            self.num_of_space += 5

    def draw_lower_middle_part(self):
        while self.num_of_letters <= self.max_end_letter_count:
            for _ in range(self.num_of_space):
                print(" ", end = "")
            for _ in range(self.num_of_letters):
                print("*", end = "")
            print()

            self.num_of_letters += 2
            self.num_of_space -= 1

    def draw_lower_part(self):
        while self.s_count > 0:
            for _ in range(self.num_of_space):
                print(" ", end = "")
            self.s_count = self.num_of_letters - self.internalSpace
            for _ in range(self.s_count // 2):
                print("*", end = "")
            for _ in range(self.internalSpace):
                print(" ", end = "")
            for _ in range(self.s_count // 2):
                print("*", end = "")
            print("")

            self.num_of_letters += 2
            self.num_of_space -= 1
            self.internalSpace += 6
