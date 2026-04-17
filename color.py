import turtle as t
import colorsys as cs


h = 0
t.bgcolor("black")
t.hideturtle()
t.speed(0)
t.pensize(3)
t.pencolor("white")

for i in range(15):
    c = cs.hsv_to_rgb(h,1,1)
    h += 0.02
    t.pencolor(c)
    t.circle(90,i)
    t.left(85)
    t.fillcolor(c)
    t.begin_fill()
    t.left(30)
    t.circle(90,70)
    t.end_fill()
    for j in range(29):
        t1 = t.clone()
        c1= cs.hsv_to_rgb(j,0.5,0.5)
        t1.pensize(1)
        t1.pencolor()
        t1.circle(180,j)
        t1.right(10)
        t1.circle(j,60)
        t1.circle(180,20)
         

 
    
    


t.done()