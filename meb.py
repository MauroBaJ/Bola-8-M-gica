import random as rd
import time as t
from datetime import datetime as dt

rd.seed(dt.now())

def answer():
    responses = [   "Si",
                    "No",
                    "Quizas",
                    "No lo creo",
                    "Es posible",
                    "No contaria con ello",
                    "Es factible",
                    "A lo mejor",
                    "Dale una oportunidad",
                    "Ni lo intentes",
                    "Tal vez",
                    "Absolutamente",
                    "Absolutamente no",
                ]
    print(rd.choice(responses))

def impresion():
    print ("____________________________________________________")
    print()
    print("       _.a$$$$$a._")
    print("      ,$$$$$$$$$$$$$.")
    print("    ,$$$$$$$$$$$$$$$$$.")
    print("   d$$$$$$$$$$$$$$$$$$$b")
    print("  d$$$$$$$$~'''~$$$$$$$$b")
    print(" ($$$$$$$p   _   q$$$$$$$)")
    print(" $$$$$$$$   (_)   $$$$$$$$")
    print(" $$$$$$$$   (_)   $$$$$$$$")
    print(" ($$$$$$$b       d$$$$$$$)")
    print("  q$$$$$$$$a._.a$$$$$$$$p")
    print("   q$$$$$$$$$$$$$$$$$$$p")
    print("    `$$$$$$$$$$$$$$$$$'")
    print("      `$$$$$$$$$$$$$")
    print("        `~$$$$$$$~'")
    print()
    print("Bola 8 Mágica")


impresion()
z = True
while z:
  print()
  print("¿Cual es tu pregunta? :")
  a = input()
  print()
  print("Interesante. Dame unos segundos para pensarlo")
  x = [ 1, 2, 3, 4, 5]
  y = rd.choice(x)
  t.sleep(y)
  answer()
  print()
  print("Deseas jugar nuevamente? S/N")
  b = input()
  if b == 'N' or b == 'n':
    z = False