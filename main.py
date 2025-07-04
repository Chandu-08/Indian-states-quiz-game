import turtle
import random
import pandas
data=pandas.read_csv("states")
screen=turtle.Screen()
screen.title("India states  quiz game")
image="india_map.gif"
screen.addshape(image)
turtle.shape(image)
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

guessed_states=[]

while len(guessed_states)<29 :
 answer_state=screen.textinput(title=f"{len(guessed_states)}/29states correct",prompt="What's another state name").title()
 all_states=data.state.to_list()
 if answer_state=="Exit":
      missed_states=[]
      for state in all_states:
          if state not in guessed_states:
              missed_states.append(state)
      new_data=pandas.DataFrame(missed_states)
      new_data.to_csv("States learn .csv")
      break
 if answer_state in all_states:
    guessed_states.append(answer_state)
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data.state==answer_state]
    t.goto(state_data.X.item(),state_data.Y.item())
    t.color(random_color())
    t.write(answer_state,font=("Arial",8,"normal"))

screen.exitonclick()