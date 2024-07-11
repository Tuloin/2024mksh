dotX,dotY,dotSize=[],[],[]
userX,userY,userSize=200.0,200.0,30.0
def setup():
    size(400,400)
    for i in range(10):
        dotX.append(random(400))
        dotY.append(random(400))
        dotSize.append(random(5,20))
                    
def draw():
    global userX,userY,userSize
    background(230,235.238)
    stroke(205,216,221)
    for x in range(0,400,50):
        line(x,0,x,400)
    for y in range(0,400,50):
        line(0,y,400,y)
    fill(255,167,7)    
    ellipse(userX,userY,userSize,userSize)
    fill(0,207,255)
    for i in range(len(dotX)):
        ellipse(dotX[i],dotY[i],dotSize[i],dotSize[i])
        if dist(userX,userY,dotX[i],dotY[i])<(userSize+dotSize[i])/2:
            if dotSize[i]!=0:userSize = sqrt(userSize**2+dotSize[i]**2)
            dotSize[i] =0
    userX=(mouseX+userX*19)/20
    userY=(mouseY+userY*19)/20
