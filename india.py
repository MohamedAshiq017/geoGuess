import turtle
import pandas
import pyperclip
screen=turtle.Screen()
screen.title("India States and Union Territories Game")
image='india.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
states_data=pandas.read_csv("india.csv")
data=pandas.DataFrame(states_data)

correct_guesses=[]
game_title="Guess the State"
while len(correct_guesses)<35:

  answer_state=screen.textinput(title=game_title,prompt="What's another state's name?").title()
  pyperclip.copy(answer_state)

  if answer_state=="Exit":
    missed=[state for state in data['state'] if state not in correct_guesses]
    # missed=[]
    # for state in data['state']:
    #   if state not in correct_guesses:
    #     missed.append(state)

    missed=pandas.DataFrame(missed,columns=["states"])
    missed.to_csv("missed_states.csv")    
    for ms in missed["states"]:
          cords=data[data.state==ms]
          turt=turtle.Turtle()
          turt.hideturtle()
          turt.penup()
          turt.goto(int(cords.x),int(cords.y))
          turt.pencolor("red")
          turt.write(ms,align="center")
    break

  if answer_state in data.state.values: 
    if answer_state not in correct_guesses:
      correct_guesses.append(answer_state) 
      game_title=f"{len(correct_guesses)}/35 States Correct"    
      cords=(data[data.state==answer_state])
      turt=turtle.Turtle()
      turt.hideturtle()
      turt.penup()
      turt.goto(int(cords.x),int(cords.y))
      turt.write(answer_state,align="center")
      screen.update()


      
screen.update()


screen.exitonclick()























