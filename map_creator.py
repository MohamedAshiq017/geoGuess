import turtle
import pandas
import pyperclip
screen=turtle.Screen()
screen.title("coordinator")
image='abc.gif'  # replace it with the map image in the gif format
screen.addshape(image)
turtle.shape(image)
screen.setup(width=screen.window_width(), height=screen.window_height())
screen.tracer(0)

data={
    "state":[],
    "x":[],
    "y":[]
    }
data= pandas.DataFrame(data)



def get_mouse_click_coor(x,y):
  state=answer_state=screen.textinput(title="coordinating",prompt="Enter state's name or 'save' to save the cordinates in the file ").title()
  if state == "Save":
    filename=screen.textinput(title="Saving info",prompt="Enter the country or state(the geographic region name):").title()
    data.to_csv(f"{filename}.csv", index=False)
    print(f"Data saved to {filename}.csv")
    screen.exitonclick()
  else:
    data.loc[len(data)] = [state, x, y]
    print(f" {state} : {x} , {y}")
    print(data)


turtle.onscreenclick(get_mouse_click_coor)




