import turtle
import pyautogui
import imageio
import os
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.title("India Flag Drawing")
screen.tracer(0)  # turn off auto updates

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Create folder for frames
if not os.path.exists("frames"):
    os.mkdir("frames")

frame_count = 0

def capture_frame():
    global frame_count
    filename = f"frames/frame_{frame_count:04d}.png"
    x0, y0 = 100, 100  # adjust based on window position
    w, h = 900, 600
    pyautogui.screenshot(filename, region=(x0, y0, w, h))
    frame_count += 1

# --- your flag drawing code below ---
pen.penup()
pen.goto(-400, 250)
pen.pendown()

pen.color("orange")
pen.begin_fill()
for _ in range(2):
    pen.forward(800)
    pen.right(90)
    pen.forward(167)
    pen.right(90)
pen.end_fill()
capture_frame()

pen.forward(167)
pen.color("green")
pen.begin_fill()
for _ in range(2):
    pen.forward(167)
    pen.left(90)
    pen.forward(800)
    pen.left(90)
pen.end_fill()
capture_frame()

pen.penup()
pen.goto(70, 0)
pen.pendown()
pen.color("navy")
pen.begin_fill()
pen.circle(70)
pen.end_fill()
capture_frame()

pen.penup()
pen.goto(60, 0)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(60)
pen.end_fill()
capture_frame()

pen.penup()
pen.goto(-57, -8)
pen.pendown()
pen.color("navy")
for i in range(24):
    pen.begin_fill()
    pen.circle(3)
    pen.end_fill()
    pen.penup()
    pen.forward(15)
    pen.right(15)
    pen.pendown()
    capture_frame()

pen.penup()
pen.goto(20, 0)
pen.pendown()
pen.begin_fill()
pen.circle(20)
pen.end_fill()
capture_frame()

pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.pensize(2)
for i in range(24):
    pen.forward(60)
    pen.backward(60)
    pen.left(15)
    capture_frame()

# --- end of drawing ---
screen.update()
turtle.done()

# --- combine frames into video ---
print("Creating video...")

with imageio.get_writer("flag.mp4", fps=20) as video:
    for i in range(frame_count):
        img = imageio.imread(f"frames/frame_{i:04d}.png")
        video.append_data(img)

print("✅ Saved as flag.mp4 — ready to play in VLC!")
