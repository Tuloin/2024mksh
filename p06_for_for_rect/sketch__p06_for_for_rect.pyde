#p06_for_for_rect
#在600*600裡放10*10共一百格
size(600,600)
background(164,255,85)
for x in range(10):
    for y in range(10):
        fill(255,100,253)
        rect(x*60,y*60,55,55)
