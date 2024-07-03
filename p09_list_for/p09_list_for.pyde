
#p09_list_for
names=['alice','Bob','Cola']
for name in names:
    print(name) 
background(0,0,255)
size(300,300)
for i in range(len(names)):
    fill(255,255,0)
    text(names[i],i*100,100)
