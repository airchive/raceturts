#!/bin/python3

from turtle import *;
from random import randint;

speed(10);
penup();
goto(-140, 140);

for step in range(15):
  write(step, align='center');
  right(90);
  forward(10);
  for up in range(8):
    pendown();
    forward(10);
    penup();
    forward(10);
  backward(170);
  left(90);
  forward(20);
  
panny = Turtle();
panny.color('red');
panny.shape('turtle');

airsit = Turtle();
airsit.color('green');
airsit.shape('turtle');

panny.penup();
panny.goto(-160, 100);

for turn in range(10):
  panny.right(36);

airsit.penup();
airsit.goto(-160, 80);

for turn in range(10):
  airsit.left(36);

for turn in range(100):
  panny.forward(randint(1,5));
  airsit.forward(randint(1,5));
  