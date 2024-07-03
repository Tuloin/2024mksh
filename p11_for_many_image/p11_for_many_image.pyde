# p11_for_many_image
def setup():
    global b,c
    size(1000,600)
    b=loadImage('TT.jpg')
    c=loadImage('IB.png')
def draw():
    global b,c
    image(b,0,0,1000,600)
    for i in range(10):
        image(c,i*100,0,100,230)
    image(c,mouseX,mouseY,100,230)
