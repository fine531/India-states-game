import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Click to get coordinates for Indian States")
image = "../R1.gif"
screen.addshape(image)
turtle.shape(image)

# List to hold the state names and their coordinates
states_data = []

# Function to get the coordinates on click and input state name
def get_mouse_click_coor(x, y):
    state_name = screen.textinput(title="State Name", prompt="Enter the state name:").title()
    states_data.append((state_name, x, y))
    print(state_name, x, y)

turtle.onscreenclick(get_mouse_click_coor)

screen.mainloop()

# Save the collected data into a CSV file
states_df = pd.DataFrame(states_data, columns=["state", "x", "y"])
states_df.to_csv("indian_states_coordinates.csv", index=False)
print("Coordinates saved to indian_states_coordinates.csv")
