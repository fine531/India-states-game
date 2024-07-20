import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("Indian States Game")

# Load the image of the map
image = "R1.gif"
screen.addshape(image)
turtle.shape(image)

# Load the CSV data
data = pandas.read_csv("./finding states  csv/indian_states_coordinates.csv")
all_states = data.state.to_list()
guessed_states = []

# Logic of the game
while len(all_states) > 0:
    answer_state = screen.textinput(title=f"{len(all_states)} / 26 states correct", prompt="Guess the next state").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("remaining_states.csv", index=False)
        break

    if answer_state in all_states:
        all_states.remove(answer_state)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)

# Keep the screen open until it is clicked
screen.exitonclick()
