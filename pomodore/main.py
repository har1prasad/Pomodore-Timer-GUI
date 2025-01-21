from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#387F39"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    label_head.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min = WORK_MIN * 60
    short_min = SHORT_BREAK_MIN * 60
    long_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:  # After 4 work sessions, take a long break
        count_down(long_min)
        label_head.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # After each work session, take a short break
        count_down(short_min)
        # label_head.place(x=135, y=75)
        label_head.config(text="Break", fg=PINK)
    else:  # Work session
        count_down(work_min)
        label_head.config(text="Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro GUI")
canvas = Canvas(width=500, height=500, background=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(250, 250, image=tomato_img)
timer_txt = canvas.create_text(250, 270, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

label_head = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
label_head.place(x=202, y=75)

button_start = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
button_start.place(x=75, y=400)

button_reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer)
button_reset.place(x=375, y=400)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_marks.place(x=250, y=400)

window.mainloop()

