import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()

screen.addshape(image)
turtle.shape(image)
my_screen_writes = []
correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess a State", prompt="What is another state?").title()

    if answer_state == "Exit":
        # states_to_learn.csv
        states_not_guessed = []
        for state in all_states:
            if state not in correct_guesses:
                states_not_guessed.append(state)

        states_df = pandas.DataFrame({
            "state": states_not_guessed
        })
        states_df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        correct_guesses.append(answer_state)
        new_state = turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        target_state = data[data.state == answer_state]
        x_coord = int(target_state.x)
        y_coord = int(target_state.y)
        state_coord = (x_coord, y_coord)
        new_state.goto(state_coord)
        new_state.write(answer_state, font=("Arial", 8, "normal"))
        my_screen_writes.append(new_state)




turtle.mainloop()


