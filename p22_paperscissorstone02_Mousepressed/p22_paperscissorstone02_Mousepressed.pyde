#p22_paperscissorstone02_Mousepressed
def setup():
    size(600,300)
def draw():
    fill(255)
    rect(0,0,300,300)
    rect(300,0,300,300)
    
    rect(400,50,100,50)#布paper
    rect(400,100,100,50)#剪刀scissor
    rect(400,150,100,50)#石頭stone
    
    textSize(30)#文字大小
    textAlign(LEFT,TOP)
    fill(0)
    text("paper",400,50)
    text("scissor",400,100)
    text("stone",400,150)
def mousePressed():
    select=-1
    if 400<mouseX<500:#在左右範圍內
        if 50<mouseY<100:select=0#上下範圍也對
        if 100<mouseY<150:select=1
        if 150<mouseY<200:select=2
    print(select)
