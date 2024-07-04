#p19_simpleSHMJ02_cos_sin)center_radias
def setup():
    size(300,300)
def draw():
    background(255)
    noFill()
    ellipse(150,150,100,100)
    fill(0)
    a=frameCount*PI/360
    ellipse(150+50*cos(a),150+50*sin(a),8,8)
