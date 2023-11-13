from turtle import Screen
from racers import Racers

screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.title('Turtle Race')

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

racer = Racers()
racer.create_racers()

is_game_on = True

while is_game_on:
    win_color = racer.turtle_race()
    if win_color:
        is_game_on = False

if user_bet == win_color:
    print(f'You won! The {win_color} turtle is the winner')
else:
    print(f'You lose! The {win_color} turtle is the winner')

screen.exitonclick()
