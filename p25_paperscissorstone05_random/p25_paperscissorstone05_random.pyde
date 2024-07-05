#p25_paperscissorstone05_random
import random
select,computer=-1,-2
def setup():
    size(600,300)
def draw():
    fill(255)
    rect(0,0,300,300)
    rect(300,0,300,300)
    for i in range(3):
        if select==i:fill(255,0,0)
        else:fill(255)
        rect(400,50+i*50,100,50)
    for c in range(3):
        if computer==c:fill(255,0,0)
        else:fill(255)
        rect(100,50+c*50,100,50)
    
    textSize(30)#文字大小
    textAlign(LEFT,TOP)
    fill(0)
    for i in range(2):
        text("paper",100+i*300,50)
        text("scissor",100+i*300,100)
        text("stone",100+i*300,150)
def mousePressed():
    global select,computer
    if 400<mouseX<500:#在左右範圍內
        computer=int(random.randrange(3))
        if 50<mouseY<100:select=0#上下範圍也對
        if 100<mouseY<150:select=1
        if 150<mouseY<200:select=2
    if select == computer:
        print("It's a tie!")
    elif (select == 2 and computer == 1) or (select == 0 and computer == 2) or (select == 1 and computer == 0):
        print("You win!")
    else:
        print("Computer wins!")
