#coding: utf-8
from sense_hat import SenseHat
import random

limite = int(input("Introduce el limite: "))
aleatorio = random.randint(1,limite)
#print aleatorio
salir = "false"

s = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def menor():
    Y = yellow
    O = nothing
    B = blue
    logo = [
    O, O, O, O, O, B, O, O, 
    O, O, O, O, B, B, O, O,
    O, O, O, B, B, O, O, O, 
    O, O, B, B, O, O, O, O,
    O, O, O, B, B, O, O, O,
    O, O, O, O, B, B, O, O,
    O, O, O, O, O, B, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def mayor():
  Y = yellow
  O = nothing
  B = blue
  logo = [
  O, O, B, O, O, O, O, O, 
  O, O, B, B, O, O, O, O,
  O, O, O, B, B, O, O, O, 
  O, O, O, O, B, B, O, O,
  O, O, O, B, B, O, O, O,
  O, O, B, B, O, O, O, O,
  O, O, B, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo
  
images = [menor, mayor]
count = 0
fallos = 0
while salir == "false":
  s.set_pixels(images[count % len(images)]())
  adivinar = int(input("¿En que número estoy pensando? "))
  
  if (adivinar != aleatorio):
    fallos = fallos + 1
    
    if (adivinar > aleatorio):
      count = 0
    
    if (adivinar < aleatorio):
      count = 1
  else:
    if (adivinar == aleatorio):
      salir = "true"
print "felicidades, has ganado"
print "Has tenido", fallos, "fallos"
