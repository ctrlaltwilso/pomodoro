from tkinter import *
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

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    start_button.config(state='normal')
    reset_button.config(state='disabled')
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    start_button.config(state='disabled')
    reset_button.config(state='normal')
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        window.attributes('-topmost', True)
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        window.attributes('-topmost', True)
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        window.attributes('-topmost', False)
        title_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks = ""
            work_sessions = math.floor(reps/2)
            for i in range(work_sessions):
                checkmarks += "✓"
            checkmark_label.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
title_label.config(bg= YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200 , height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./images/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="White", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.config(bg="White", font=(FONT_NAME, 12), borderwidth=0)
start_button.grid(column= 0, row=2)

reset_button = Button(text="Reset")
reset_button.config(bg="White", font=(FONT_NAME, 12), borderwidth= 0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(font= 15)
checkmark_label.config(bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)

window.mainloop()