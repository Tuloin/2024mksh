# p13_for_many_image_list_def_mousePressed
def setup():
    global b,c
    size(1000,600)
    b=loadImage('TT.jpg')
    c=loadImage('IB.png')
def draw():
    global b,c
    image(b,0,0,1000,600)
    for i in range(len(x)):
        image(c,x[i],y[i],200,230)
    image(c,mouseX-100,mouseY-100,200,230)
x = []#x=[0]*10
y = []#y=[0]*10
#N=0
def mousePressed():
    x.append(mouseX-100) #global N
    y.append(mouseY-100) #x[N],y[N]=mouseX,mouseY
    #N += 1
