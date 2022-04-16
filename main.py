# Complete By Kebe Mario abd Loritha)
# You can do the rest!
import timeit
import time,os

def books():
  print("Our Books section is coming soon,You might need to go into an actual store until then.Sorry\n")
  time.sleep(3)
def movie():
  print("Yeah, sorry. It's Netflix or your local multiplex until our developer are being fat and lazy. Sorry.\n")
  time.sleep(3)
def account():
  pass
while(True):
  print("\t\tWELCOME TO SHERWOOD PRIME")
  print("--Enter the number to make your selection--\n")#some edits
  print("Press 1 for Books")
  print("Press 2 for Movies")
  print("Press 3 for My Account")
  print("Press any other number to exit")
  menuSelection =input("> ")
  if(menuSelection =="1"):
    books()
  elif(menuSelection=="2"):
    movie()
  elif(menuSelection=="3"):
    account()
  else:
    print("ERROR: Unknown selection,Try again")

time.sleep(1)
os.system('Clear')
