t=200
def myStar(x,y,t):
    cSize=t#dist(mouseX,mouseY,250,200)*2
    noFill()
    ellipse(x,y,cSize,cSize)
    fill(193,33,33)
    ellipse(x,y,40,40)
x,y=[],[]
def setup():
    size(500,500)
    for k in range(10):
        x.append(random(500))
        y.append(random(500))
def draw():
    global t
    background(0)
    stroke(92,0,0)
    strokeWeight(6)
    t -= 2
    if t==40: t=200
    for i in range(len(x)):
        myStar(x[i],y[i],t)
    
