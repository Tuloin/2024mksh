#p21_paperscissor_stone01_text
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
