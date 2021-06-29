from tkinter import *
import random


root = Tk()
root.title("Rock, Paper and Scissor")
root.geometry("500x600")
# Structure
mainContent = Frame(root, width="400", height="400")
buttonDiv = Frame(root, width="400", height="200")
mainContent.pack(side=TOP)
buttonDiv.pack(side=BOTTOM)
l = Label(mainContent,text="Welcome",font=('montserrat',26))
l.pack()
l2 = Label(mainContent,text="",font=('montserrat',20))
l2.pack()

button1 = Button(buttonDiv,
                 text="Rock",
                 bg="white",
                 fg="black",
                 pady="20",
                 padx="40",
                 bd="10",
                 font=("montserrat", 22))
button2 = Button(buttonDiv,
                 text="Paper",
                 bg="white",
                 fg="black",
                 pady="20",
                 padx="40",
                 bd="10",
                 font=("montserrat", 22))
button3 = Button(buttonDiv,
                 text="Scissor",
                 bg="white",
                 fg="black",
                 pady="20",
                 padx="40",
                 bd="10",
                 font=("montserrat", 22))
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=RIGHT)
# Game / Functions
# AI
ai_input = None


def ai_play():
    options = ["Rock", "Paper", "Scissor"]
    randNum = random.randint(0, 2)
    global ai_input
    ai_input = options[randNum]

# USER
userInput = None


def rock():
    global userInput
    userInput = "Rock"
    ai_play()
    check_win()
    l2.config(text=f'You chose {userInput} and Ai chose {ai_input}')

def paper():
    global userInput
    userInput = "Paper"
    ai_play()
    check_win()
    l2.config(text=f'You chose {userInput} and Ai chose {ai_input}')


def scissor():
    global userInput
    userInput = "Scissor"
    ai_play()
    check_win()
    l2.config(text=f'You chose {userInput} and Ai chose {ai_input}')


def check_win():
    if userInput == "Rock" and ai_input == "Scissor":
        l.config(text="user WINS")
    elif userInput == "Paper" and ai_input == "Rock":
        l.config(text="user WINS")
    elif userInput == "Scissor" and ai_input == "Paper":
        l.config(text="user WINS")
    elif userInput == ai_input:
        l.config(text="Tie")
    else:
        l.config(text="Ai WINS")
        print(ai_input)
        print(userInput)


button1.config(command=rock)
button2.config(command=paper)
button3.config(command=scissor)

root.mainloop()
