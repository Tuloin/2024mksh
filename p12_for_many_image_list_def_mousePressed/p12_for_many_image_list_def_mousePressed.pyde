# p12_for_many_image_list_def_mousePressed
def setup():
    global b,c
    size(1000,600)
    b=loadImage('TT.jpg')
    c=loadImage('IB.png')
def draw():
    global b,c
    image(b,0,0,1000,600)
    for i in range(10):
        image(c,x[i],y[i],200,230)
    image(c,mouseX,mouseY,200,230)
x = [0]*10
y=  [0]*10
N=0
def mousePressed():
    global N
    x[N],y[N]=mouseX,mouseY
    N += 1
