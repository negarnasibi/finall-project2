import random
import turtle
import time


colors=["red","yellow","green","blue","pink","purple","lightblue","lightpink"]
class Fractal:
    def __init__(self):
       pass
            
    def drow(self):
        sides=int(input("Enter a sides:"))
        length=int(input("Enter a length:"))
        repetition=int(input("Enter a repetition:"))
        t=turtle.Pen()
        t.speed(100)
        for g in range(repetition):
            for i in range(sides):
                t.color(random.choice(colors))
                t.forward(length)
                t.left(360/sides)
            t.left(10)   
       

fractal1=Fractal()
t1=time.time()
fractal1.drow()
t2=time.time()
t3=t2-t1
rezult=round(t3,2)
print("performance time is %s second" % rezult)


    
