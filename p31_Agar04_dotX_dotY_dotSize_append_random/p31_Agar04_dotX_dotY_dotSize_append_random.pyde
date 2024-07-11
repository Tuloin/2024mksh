dotX,dotY,dotSize=[],[],[]
userX,userY=200.0,200.0
def setup():
    size(400,400)
    for i in range(10):
        dotX.append(random(400))
        dotY.append(random(400))
        dotSize.append(random(3,20))
                    
def draw():
    global userX,userY
    background(230,235.238)
    stroke(205,216,221)
    for x in range(0,400,50):
        line(x,0,x,400)
    for y in range(0,400,50):
        line(0,y,400,y)
    fill(255,167,7)    
    ellipse(userX,userY,100,100)
    fill(0,207,255)
    for i in range(len(dotX)):
        ellipse(dotX[i],dotY[i],dotSize[i],dotSize[i])
    userX=(mouseX+userX*19)/20
    userY=(mouseY+userY*19)/20
