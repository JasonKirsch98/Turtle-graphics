#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:39:56 2017

@author: jasonkirschsmacbookpro
"""

import turtle #Import turtle module
import random #import random module


def pick_color(): 
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors

colors = pick_color()
squares = int(input("Please enter a value greater than 0, up and including 10:"))
if (squares < 1 or squares > 10):
    print("Error, please enter a value 1-10:")
else:
    window = turtle.Screen() #Create a screen
    turt = turtle.Turtle() #Create a turtle
    for i in range(squares): #For each square
        turt.fillcolor(str(colors[i])) #Set color
        turt.pencolor(str(colors[i]))
        turt.goto(-200+10*i,-200+10*i) #Send to bottom left corner
        turt.pendown()
        turt.begin_fill()
        turt.goto(-200+10*i,200-10*i) #Upper left
        turt.goto(200-10*i,200-10*i) #Upper Right
        turt.goto(200-10*i,-200+10*i) #Lower Right
        turt.goto(-200+10*i,-200+10*i) #Back to lower left
        turt.end_fill()
        turt.penup() #Pick up pen
    window.exitonclick() #Close window once clicked
    