import tkinter as tk
import math
import random
import time

root = tk.Tk()
root.geometry('800x800')
root.resizable(False, False)
root.configure(bg='yellow')

x_pos=400
y_pos=400
label = tk.Label(root, bg='red', width=2, height=1)
label.place(x=x_pos, y=y_pos)

label_input = tk.Label(root, text='Enter your input')
label_input.place(x=400, y=750)
label_controller =tk.Entry(root)
label_controller.place(x=400, y=770)

label1 = tk.Label(root, bg='black', width=1, height=1)
label1.place(x=200, y=200)
x_pos1=400
y_pos1=600
moving_label = tk.Label(root, bg='green', width=8, height=1)
moving_label.place(x=x_pos1, y=y_pos1)

x_pos2 = 300
y_pos2 = 700
ai_label = tk.Label(root, bg='blue', width=2, height=1)
ai_label.place(x=x_pos2, y=y_pos2)

current_move = None

value=""
new_x=random.randint(0,700)
new_y=random.randint(0, 700)
new_x2=random.randint(0, 700)
new_y2=random.randint(0, 700)

lives = 5
label8 = tk.Label(root, text=f'Lives: {lives}')
label8.place(x=0, y=780)

def start_timer():
   global elapsed_time
   elapsed_time = 0
   update_timer()
def update_timer():
   global elapsed_time
   minutes, seconds = divmod(elapsed_time, 60)
   timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
   elapsed_time += 1
   timer_label.after(1000, update_timer)
timer_label = tk.Label(root, font=('arial', 20, 'bold'), bg='black',
                      fg='white')
timer_label.place(x=700, y=40)
start_timer()


def ai_chaser():
  global x_pos2, y_pos2
  global new_x2, new_y2
  x = ai_label.winfo_x()
  y = ai_label.winfo_y()
  if (new_x-new_x2)<0:
      new_x2 = x - 8
  if (new_x-new_x2)>0:
      new_x2 = x + 8
  if (new_y-new_y2)<0:
      new_y2 = y - 8
  if (new_y-new_y2)>0:
      new_y2 = y + 8
  ai_label.place(x=new_x2, y=new_y2)
  root.after(100, ai_chaser)

  print(new_x, new_y)

def moving_object():
  global x_pos1, y_pos1
  global new_x1, new_y1
  x = moving_label.winfo_x()
  y = moving_label.winfo_y()
  if x > 0:
      new_x1 = x - 10  # move object to the left
      new_y1 = y_pos1  # maintain the same y position
  else:
      new_x1 = 800  # reset the object to the right side of the screen
      new_y1 = y_pos1  # maintain the same y position
  moving_label.place(x=new_x1, y=new_y1)
  root.after(10, moving_object)

def hit_boundary(x1, y1):
  global value
  if x1<=0 or y1<=0 or x1>=780 or y1>=780:
      label3 = tk.Label(root, text='Hit Boundary', bg='red')
      label3.place(x=600, y=600)
      game_over()


def hit_label1(x1, y1):
  if (180<x1<213) and (180<y1<220):
      label2 = tk.Label(root, text='hit wall', font=('arial', 20, 'bold'),
                        bg='white')
      label2.place(x=500, y=500)
      lose_life()
def left_move():
  global current_move
  global x_pos, y_pos
  global new_x, new_y
  x = label.winfo_x()
  y = label.winfo_y()
  new_x = x - 15
  new_y = y
  label.place(x=new_x, y=new_y)
  hit_label1(new_x, new_y)
  hit_boundary(new_x, new_y)
  if current_move == 'left':
      root.after(100, left_move)
  else:
      current_move = None
def right_move():
  global current_move
  global x_pos, y_pos
  global new_x, new_y
  x = label.winfo_x()
  y = label.winfo_y()
  new_x = x + 15
  new_y = y
  label.place(x=new_x, y=new_y)
  hit_label1(new_x, new_y)
  hit_boundary(new_x, new_y)
  if current_move == 'right':
      root.after(100, right_move)
  else:
      current_move = None
def forward_move():
  global current_move
  global x_pos, y_pos
  global new_x, new_y
  x = label.winfo_x()
  y = label.winfo_y()
  new_x = x
  new_y = y - 15
  label.place(x=new_x, y=new_y)
  hit_label1(new_x, new_y)
  hit_boundary(new_x, new_y)
  if current_move == 'forward':
      root.after(100, forward_move)
  else:
      current_move = None
def back_move():
  global current_move
  global x_pos, y_pos
  global new_x, new_y
  x = label.winfo_x()
  y = label.winfo_y()
  new_x = x
  new_y = y + 15
  label.place(x=new_x, y=new_y)
  hit_label1(new_x, new_y)
  hit_boundary(new_x, new_y)
  if current_move == 'back':
      root.after(100, back_move)
  else:
      current_move = None
previous_length = 0
def control_square():
  global previous_length
  global current_move
  global label_controller
  global value
  value = label_controller.get()
  if value != "":

        if value[-1] == 'a' or value[-1] == 'A':
          left_move()
          current_move = 'left'
        elif value[-1] == 'd' or value[-1] == 'D':
          right_move()
          current_move = 'right'
        elif value[-1] == 'w' or value[-1] == 'W':
          forward_move()
          current_move = 'forward'
        elif value[-1] == 's' or value[-1] == 'S':
          back_move()
          current_move = 'back'


  root.after(100, control_square)
def hit_object():
  if (-104<(new_x1-new_x)<26) and (-20<(new_y1-new_y)<20):
      print("Moving object hit")
      lose_life()
  root.after(100, hit_object)
def ai_caught():
  if (-26<(new_x-new_x2)<26) and (-26<(new_y-new_y2)<26):
      print("ai caught")
      lose_life()
  root.after(100, ai_caught)


def lose_life():
  global lives
  lives -= 1
  label8 = tk.Label(root, text=f'Lives: {lives}')
  label8.place(x=0, y=780)

  if lives == 0:
      game_over()
def game_over():
  root.destroy()
  new_window = tk.Tk()
  new_window.geometry('800x800')
  new_window.title('Game Over')
  label7 = tk.Label(new_window, text='GAME OVER',
                    font=('arial', 30), fg='red')
  label7.place(x=400, y=400)
  label10 = tk.Label(new_window, text=f'You lasted {elapsed_time} seconds!!')
  label10.place(x=400, y=600)


  new_window.mainloop()
control_square()
moving_object()
hit_object()
ai_chaser()
ai_caught()

root.mainloop()
aaaawdwdwwwwwwwwwwwww