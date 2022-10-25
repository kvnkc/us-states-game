from tkinter import Y
import turtle
import pandas

screen = turtle.Screen()
screen.title(f'U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle.tracer(0)
correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(
        title=f'{len(correct_guess)}/50 States correct', prompt="What's another state's name?: ").title()

    data = pandas.read_csv('50_states.csv')

    states = data.state.to_list()

    # Exits the game and converts missing states into a separate list and csv
    if answer_state == 'Exit':
        missing_states = []
        for state in states:
            if state not in correct_guess:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    # Checks if title_amswer is one of the states in all the states in the 50_states.csv
    if answer_state in states:
        coord = data[data.state == answer_state]
        x_coord = int(coord.x)
        y_coord = int(coord.y)
        turtle.penup()
        turtle.goto(x_coord, y_coord)
        turtle.write(answer_state)
        correct_guess.append(answer_state)
