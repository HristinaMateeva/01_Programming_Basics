from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAINING_RATE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + Thoroughbred.TRAINING_RATE > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += Thoroughbred.TRAINING_RATE
