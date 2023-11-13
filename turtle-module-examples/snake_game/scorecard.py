from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_game\\data.txt') as data:
            self.high_score = int(data.read())
        # self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game\\data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scorecard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scorecard()
