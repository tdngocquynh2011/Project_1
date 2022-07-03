from tkinter import *
import random
root = Tk()
root.title("Rock Paper Scissor")
width = 600
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)
root.config(bg="#006699")

player_rock = PhotoImage(file='rock-user.png')
player_paper = PhotoImage(file='paper-user.png')
player_scissors = PhotoImage(file='scissors-user.png')
comp_rock = PhotoImage(file = 'rock-comp.png')
comp_paper = PhotoImage(file = 'paper-comp.png')
comp_scissors = PhotoImage(file = 'scissors-comp.png')
start = PhotoImage(file = 'start.png').subsample(5)
win = PhotoImage(file = 'win.png').subsample(5)
draw = PhotoImage(file = 'draw.png').subsample(5)
lose = PhotoImage(file = 'lose.png').subsample(5)

player_img = Label(root, image = player_rock,bg = '#4080bf')
player_img.grid(row = 2,column = 1,padx = 30,pady =30)
comp_img = Label(root,image = comp_rock,bg = '#4080bf')
comp_img.grid(row = 2, column = 3,padx = 30,pady =30)
# Lbl Player
lbl_player = Label(root, font = ("Arial", 15),text = 'Player',bg='#0088cc',fg='white')
lbl_player.grid(row =1,column =1)
# Lbl Comp
lbl_comp = Label(root, font = ("Arial", 15),text = 'Computer',bg='#0088cc',fg='white')
lbl_comp.grid(row =1,column =3)
# Score
player_score = Label(root, text = '0', font = ('Arial', 30),bg='#0088cc',fg = 'white')
breaklbl = Label(root,text='-',font=('Arial',30),bg = '#0088cc',fg = 'white')
comp_score = Label(root, text = '0',font=('Arial',30),bg='#0088cc',fg='white')
player_score.grid(row=3,column=1)
breaklbl.grid(row=3,column=2)
comp_score.grid(row=3,column=3)

#Message
msg = Label(root, font = ("Arial", 15),bg='#0088cc',fg='white')
msg.grid(row=2,column=2)
msg.configure(image=start)

#Update Player Score
def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = score

#Update Computer Score
def updateCompScore():
    score = int(comp_score['text'])
    score += 1
    comp_score['text'] = score

#Logic
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()

def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()

def Scissors():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissors)
    MatchProcess()

def MatchProcess():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_img.configure(image=comp_rock)
        ComputerRock()
    elif comp_choice == 2:
        comp_img.configure(image=comp_paper)
        ComputerPaper()
    else:
        comp_img.configure(image=comp_scissors)
        ComputerScissors()
    
def ComputerRock():
    if player_choice == 1:
        msg.configure(image = draw)
    elif player_choice == 2:
        msg.configure(image = win)
        updatePlayerScore()
    else:
        msg.configure(image = lose)
        updateCompScore()

def ComputerPaper():
    if player_choice == 1:
        msg.configure(image = lose)
        updateCompScore()
    elif player_choice == 2:
        msg.configure(image=draw)
    else:
        msg.configure(image = win)
        updatePlayerScore()

def ComputerScissors():
    if player_choice == 1:
        msg.configure(image = win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image = lose)
        updateCompScore()
    else:
        msg.configure(image=draw)

def ExitApp():
    root.destroy()
    exit()

sm_player_rock = player_rock.subsample(3, 3)
rock = Button(root, image = sm_player_rock, command=Rock,bg='#336699')
rock.grid(row = 4, column = 1)

sm_player_paper = player_paper.subsample(3, 3)
paper = Button(root, image = sm_player_paper, command=Paper,bg='#336699')
paper.grid(row = 4, column = 2)

sm_player_scissors = player_scissors.subsample(3, 3)
scissors = Button(root, image = sm_player_scissors, command=Scissors,bg='#336699')
scissors.grid(row = 4, column = 3)

btn_quit = Button(root, text = "Quit",command=ExitApp)
btn_quit.grid(row=5,column=2)


root.mainloop()