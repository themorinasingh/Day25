import turtle
from turtleClass import my_turtle
from datafile import state_dict
import pandas

#TODO Screen Setup
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(height=520)

#TODO Turtle setup
state_writer = my_turtle()
score_keeper = my_turtle()

#ToDO setup the game, i.e

game_is_on = True
state_count = 0
states_guessed = []

#creating a new list states to learn
states_to_learn = []

while game_is_on or state_count < 50:

    state_name = screen.textinput(title=f"Guess The State {state_count} /50", prompt="What's another state name?").title()

    if state_name.title() in state_dict and state_name not in states_guessed:
        state_writer.move_and_write(state_dict[state_name], state_name)
        states_guessed.append(state_name)
        state_count += 1

    elif state_name == "Exit":
        game_is_on = False
        break

    elif state_name in states_guessed or state_name not in state_dict:
        continue




for state in state_dict:
    if state not in states_guessed:
        states_to_learn.append(state)

states_to_learn = pandas.DataFrame(states_to_learn)
states_to_learn.to_csv("States Names To learn.csv")


