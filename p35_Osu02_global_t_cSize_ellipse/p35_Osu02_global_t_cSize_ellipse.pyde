#漸進環收縮
t=200
def setup():
    size(500,400)
def draw():
    global t
    background(0)
    stroke(92,0,0)
    strokeWeight(6)
    noFill()
    cSize=t#dist(mouseX,mouseY,250,200)*2
    t -= 2
    if t==40: t=200
    ellipse(250,200,cSize,cSize)
    fill(193,33,33)
    ellipse(250,200,40,40)
