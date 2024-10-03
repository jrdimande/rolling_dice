import random
class Dice:
    def __init__(self, num_faces = 6):
        self.num_faces = num_faces
        self.result = None

    def roll(self):
        self.result = random.randint(1,self.num_faces)

    def show_result(self):
        if self.result is None:
            return "O dado ainda não foi lançado."
        else:
            return f"O resultado do lançamento foi: {self.result}"

dice = Dice()
dice.roll()
print(dice.show_result())