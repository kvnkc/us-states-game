import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(
        title='Guess the State', prompt="What's another state's name?: ")
    title_answer = answer_state.title()

    data = pandas.read_csv('50_states.csv')
    coord = data[data.state == title_answer]
    x_coord = coord.x
    y_coord = coord.y
    states = data.state.to_list()

    for state in states:
        if title_answer == state:
            print(state)
        elif title_answer != state:
            game_is_on = False

    print(coord)


screen.exitonclick()
