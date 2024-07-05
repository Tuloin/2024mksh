#p22_paperscissorstone02_Mousepressed
select=-1
def setup():
    size(600,300)
def draw():
    a= loadImage("paper.png")
    b= loadImage("scissor.png")
    c= loadImage("stone.png")
    fill(255)
    rect(0,0,300,300)
    rect(300,0,300,300)
    
    if select==0:fill(255,0,0)
    else:fill(255)
    rect(400,50,100,50)#布paper
    if select==1:fill(255,0,0)
    else:fill(255)
    rect(400,100,100,50)#剪刀scissor
    if select==2:fill(255,0,0)
    else:fill(255)
    rect(400,150,100,50)#石頭stone
    image(a,400,50,100,50)
    image(b,400,100,100,50)
    image(c,400,150,100,50)
def mousePressed():
    global select
    if 400<mouseX<500:#在左右範圍內
        if 50<mouseY<100:select=0#上下範圍也對
        if 100<mouseY<150:select=1
        if 150<mouseY<200:select=2
    print(select)
