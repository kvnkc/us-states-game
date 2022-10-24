from tkinter import Y
import turtle
import pandas

screen = turtle.Screen()
screen.title(f'U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(
        title=f'{len(correct_guess)}/50 States correct', prompt="What's another state's name?: ")
    title_answer = answer_state.title()

    data = pandas.read_csv('50_states.csv')

    states = data.state.to_list()

    if title_answer in states:
        coord = data[data.state == title_answer]
        x_coord = int(coord.x)
        y_coord = int(coord.y)
        turtle.penup()
        turtle.goto(x_coord, y_coord)
        turtle.write(title_answer)
        correct_guess.append(answer_state)

        print(coord)
        print(x_coord)
        print(y_coord)


screen.exitonclick()
