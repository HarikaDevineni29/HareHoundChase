import turtle
from tkinter import *

def SetHarePos(x,y):
    hare.up()
    hare.setpos(x,y)
    hare.down()
    GetHoundPos()
def SetHoundPos(x,y):
    hound.up()
    hound.setpos(x,y)
    hound.down()
    Chase()
def GetHarePos():
    messagebox.showinfo("Hare Position","Click on the screen to set hare position")
    win.onclick(SetHarePos)
def GetHoundPos():
    messagebox.showinfo("Hound Position","Click on the screen to set hound position")
    win.onclick(SetHoundPos)

def validchase(hare_y,hound_y):
    hare_x = round(hare.xcor(),0)
    hound_x = round(hound.xcor(),0)
    if hare_x > (WIN_SIZE[0]/2):
        if hare_vel > hound_vel:
            return -3
        elif hare_vel < hound_vel: #and hare_y == hound_y:
            return -2
    elif hare_y == hound_y:
        if hare_x == hound_x:
            return -1
        elif hare_vel == hound_vel:
            return -4
    return 1

def Chase():
    hare_y = round(hare.ycor(),0)
    hound_y = round(hound.ycor(),0)
    valid = 1
    while valid == 1:
        hound_y = round(hound.ycor(),0)
        valid = validchase(hare_y,hound_y)
        win_size = win.screensize()
        if hare.xcor() or hound.xcor() == win_size[0]:
            win.screensize((win_size[0] + 25),win_size[1])
        hound.seth(hound.towards(hare))
        hound.forward(hound_vel)
        hare.forward(hare_vel)
    if valid == -1:
        p = hound.pos()
        hare.write(str(p),font = ("Arial",20,"normal"))
        messagebox.showinfo("Chase Ends","Hound caught the hare")
    elif valid == -4:
        messagebox.showinfo("Chase Ends","Never ending...both at same pace!!")
    elif valid == -2:
        messagebox.showinfo("Chase Ends","Hare and Hound meet at point")
    elif valid == -3:
        messagebox.showinfo("Chase Ends","Hare is too fast!Hare Wins!!")

win = turtle.Screen()
win.bgcolor("green")
WIN_SIZE = (2000,2000)
win.setup(WIN_SIZE[0],WIN_SIZE[1])
hare = turtle.Turtle()
hound = turtle.Turtle()

hare.shape("triangle")
hound.shape("circle")
hare.pensize(5)
hound.pensize(5)
hare.pencolor("yellow")
hare.fillcolor("yellow")

hare_vel = simpledialog.askinteger("input","Enter hare velocity")
hound_vel = simpledialog.askinteger("input","Enter hound velocity")
while hare_vel > 10:
    hare_vel /= 10
while hound_vel > 10:
    hound_vel /= 10
hare.speed(hare_vel)
hound.speed(hound_vel)

GetHarePos()

turtle.done()
