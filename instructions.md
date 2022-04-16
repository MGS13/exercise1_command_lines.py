# Exercise 01: Creating Command Line Menus

One of the key things you need to be able to do, when you're creating a real piece of software, is build a really user-friendly interface. Normally that means a GUI of some kind… but when you're attempting an NEA you often don't have the time (or the patience) to build that - so /*how*/ do we build a decent user interface in the `command line`?

You'll be using `print`, `input` and `while` loops.

## Jump in the Delorean

Turns out those überNerds from the 80s already worked out how to make decent menus when all you have is some text. Let's take a look at the menu for a command-line social network.

```
WELCOME TO BOOKFACE
-------------------
Press 1 to create an account
Press 2 to log into an existing account
Press any other key to exit

>

```

I presume you'd know what to do here as this is a good command line user interface, but ***what*** makes this a good example?

Well, it's ***clear*** exactly what to do next, press a button. It's also ***simple***, there's not a lot to type in that can go wrong. How is this being achieved in code?

```python
while(True):
  print("WELCOME TO BOOKFACE")
  print("-------------------")
  print("Press 1 to create an account")
  print("Press 2 to log in to an existing account")
  print("Press any other key to exit")
  print("")

  menuSelection = input("> ")
```

So quite simple really - we're using a `while(True)` loop to make sure that the program constantly returns to the main menu and prompts the user to select a /*number*/, there's not a lot that can go wrong after that as long as you use ***selection*** correctly. Every line of code that's indented at least once from this point forward becomes part of the loop.

Don't forget that whilst the `while(True)` loop works here, it's not good practise to use a while loop in this way. Really it should be self terminating, the brackets should contain a condition that /*will*/ end. We're using it in a bit of a Frankenstein way, but hey-ho, it's fine for GCSE.

## IF Statements for the Win

The next step is to get some ***selection*** built into the code, we'll use an `if` statement as well as some `elif` and `else` to decide what to do for each of the possible values of `menuSelection`.

Notice that in the conditions we're using quotes around the numbers, this is because we haven't /*cast*/ the input, because we're not doing any maths with it.

```python
while(True):
  print("WELCOME TO BOOKFACE")
  print("-------------------")
  print("Press 1 to create an account")
  print("Press 2 to log in to an existing account")
  print("Press any other key to exit")
  print("")

  menuSelection = input("> ")

  if(menuSelection=="1"):
    createAccount()
  elif(menuSelection=="2"):
    logIn()
  else:
    print("ERROR: Unknown selection, try again")
```

You might be wondering "What's createAccount and logIn?" - good question! These are calls to subroutines that we haven't written yet, we'll deal with that in a minute, but do make sure that the names of the subroutines are sensible and clearly explain what they are going to do. They just help us to make the code a bit neater and easier to understand.

## Using the Time and OS Libraries for Niceness

If you go and run the code we've got at the moment it wouldn't feel quite right. The reason for this is that the selection happens immediately and resets itself in the loop. It would be really nice if we paused for a second or so after displaying some text, and maybe even clean up the screen every time something new was about to happen.

We can do this quite easily with two libraries, first we'll have to import them so we can use the code, but afterwards we only really require two of their functions. `time.sleeps(1)` will pause the execution of the code for one second, and then `os.system('clear')` will clear up all the text in the terminal so we can start afresh.

```python
import time, os

while(True):
  print("WELCOME TO BOOKFACE")
  print("-------------------")
  print("Press 1 to create an account")
  print("Press 2 to log in to an existing account")
  print("Press any other key to exit")
  print("")

  menuSelection = input("> ")

  if(menuSelection=="1"):
    createAccount()
  elif(menuSelection=="2"):
    logIn()
  else:
    print("ERROR: Unknown selection, try again")

  time.sleep(1)
  os.system('clear')

```

So, we've popped those two lines at the end of the loop  and this will make sure that whatever happens in the loop remain on screen for one second when it's done then clears the screen before showing the menu again. You can use those two lines anywhere you need a message to stay on the screen for a time before clearing the screen again.

/*Note*/: If you're doing this on Windows, using something like ***IDLE*** in your NEA time then `os.system('clear')` doesn't work, and you should use `os.system('cls')` instead.

## Subroutines Make it Simpler to Plan

The last step to building any user interface is to set it up ready for your next steps of development, we've already used selection to tell the program to take us to two subroutines but we need to at least define them before the program will run successfully. There's a really cheeky way to do this using the `pass` command. Take a look at the finished code.

```python
import time, os

def createAccount():
  pass

def logIn():
  pass

while(True):
  print("WELCOME TO BOOKFACE")
  print("-------------------")
  print("Press 1 to create an account")
  print("Press 2 to log in to an existing account")
  print("Press any other key to exit")
  print("")

  menuSelection = input("> ")

  if(menuSelection=="1"):
    createAccount()
  elif(menuSelection=="2"):
    logIn()
  else:
    print("ERROR: Unknown selection, try again")

  time.sleep(1)
  os.system('clear')
```

So what does `pass` do exactly? Well it's a placeholder, the interpreter sees `pass` and just moves along. It's a really useful bit of code to remember when you're trying to build something complicated and haven't got around to writing the code for another bit yet - it even works in loops!

If you're working on the code for your NEA project this point is a good place to pause and think about the next steps, you've got a working, effective user interface with placeholders in place for your next steps.

---

## Your Task

You have been asked to design a GCSE NEA style menu for a new shopping website, Sherwood Prime. Use the techniques above to build a menu that replicates the examples below.

1. When the program runs for the first time this splash screen should be shown for two seconds, before clearing the screen and showing the menu

```

Welcome to

 SHERWOOD
  PRIME

One stop Shopping
```

2. The menu should then display, and should have the following options

```
        S H E R W O O D   P R I M E
-- Enter the number to make your selection --

1. Books
2. Movies
3. My Account
```

3. If the user enters 1 then this message should be displayed for two seconds before returning to the main menu
```
Our books section is coming soon, you might need to go into an actual store until then. Sorry.
``` 

4. If the user enters 2 then this message should be displayed for two seconds before returning to the main menu

```
Yeah, sorry. It's Netflix or your local multiplex until our developer sorts themselves out. Sorry.
```

5. If the user selects option 3 then your subroutine should contain only the `pass` command so should just reload the menu

## Extension

6. For extra credit why not add an option to log out of the program, you may need to extend your menu and think about researching the `exit()` command


