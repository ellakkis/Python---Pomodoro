from tkinter import *
from PIL import Image, ImageTk
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET -----------------------------
def reset_timer():
  global reps
  reps = 0
  root.after_cancel(timer)
  lbl_title.config(text="Timer", fg=GREEN)
  lbl_check.config(text="")
  canvas.itemconfig(lbl_timer, text=f"00:00")

# ------------------------- TIMER MECHANISM -------------------------- # 
def start_timer():
  global reps
  reps += 1
# if it is 1st/3rd/5th/7th rep
  if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    lbl_title.config(text="Work", fg=GREEN)
    countdown(WORK_MIN * 60)
  elif reps == 2 or reps == 4 or reps == 6:
    lbl_title.config(text="5 min break", fg=PINK)
    countdown(SHORT_BREAK_MIN * 60)
  elif reps == 8:
    lbl_title.config(text="20 min break", fg=RED)
    countdown(LONG_BREAK_MIN * 60)
# ------------------ COUNTDOWN MECHANISM ---------------------------- # 
def countdown(count):
  count_min = math.floor(count / 60)
  count_sec = count % 60
  
  canvas.itemconfig(lbl_timer, text="{:02d}:{:02d}".format(count_min, count_sec))
  global timer
  if count > 0:
    timer = root.after(1000, countdown, count - 1)
  else:
    mark = ""
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
      mark += "✓"
    lbl_check.config(text=mark)
    start_timer()
  
   
        




  
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.configure(padx=20, pady=20, background=YELLOW)
root.minsize(width=200, height=200)
root.title("Pomodoro")

canvas = Canvas(width=200, height=226, highlightthickness=0, bg=YELLOW)

# TITLE lable
lbl_title = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
lbl_title.grid(column=1, row=0)

# image
tomato = PhotoImage(file="tomato.png")
canvas.create_image(101, 111, image=tomato)
canvas.grid(column=1, row=1)

# tomato timer lable
lbl_timer = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME,'20','bold'), fill=YELLOW)

# 2 buttons reset/start
btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column=0, row=3)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=3, row=3)

# checkmarks labels
lbl_check = Label(fg=GREEN, font=(FONT_NAME,'20','bold'), bg=YELLOW)
lbl_check.grid(column=1, row=3)






root.mainloop()