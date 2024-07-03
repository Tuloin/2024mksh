#p10_setup_loadImage_draw_image_global
def setup():
    global b,c,d #global就像變數
    size(1000,667)  
    c=loadImage('ya.jpg')
    b=loadImage('bu.png')
    d=loadImage('de.png')
def draw():
    global b,c,d
    image(c,0,0,1000,667)
    if mousePressed:
        image(d,mouseX-400,mouseY-350)
    else:
        image(b,mouseX-100,mouseY-100)
