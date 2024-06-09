import turtle
import math

tata = turtle.Turtle()
x=100

tata.fillcolor("lightblue") #Define a cor com a qual será feita a pintura
tata.begin_fill() #Diz que a partir daqui a área que for desenhada será pintada
for i in range(2):     ##casa
    tata.forward(2*x)
    tata.left(90)
    tata.forward(x)
    tata.left(90)
tata.end_fill() #Indica o terminou a definição da área a ser pintada e pinta

tata.fillcolor("blue") #Define a cor com a qual será feita a pintura
tata.begin_fill()
tata.forward(x/3) ##porta
tata.left(90)
tata.forward(2*x/3)
tata.right(90)
tata.forward(x/3)
tata.right(90)
tata.forward(2*x/3)
tata.end_fill()

##janela
tata.left(90)
tata.forward(x/5)
tata.left(90)
tata.up()
tata.forward(x/3)
tata.down()
tata.fillcolor("yellow")
tata.begin_fill()
for i in range(4):
    tata.forward(x/3)
    tata.right(90)
tata.end_fill()


    
##telhado
tata.right(180)
tata.up()
tata.forward(x/3)
tata.down()
tata.left(90)
tata.forward(8*x/15)

tata.left(90)
tata.up()
tata.forward(x/3)
tata.down()
tata.begin_fill()
for i in range(4):
    tata.forward(x/3)
    tata.right(90)
    
tata.end_fill()
tata.right(180)
tata.up()
tata.forward(x/3)
tata.down()


tata.left(90)
tata.forward(3*x/5)
tata.left(90)
tata.forward(x)
tata.right(90)
tata.fillcolor("red")
tata.begin_fill()
tata.forward(x/2)

tata.left(135)
tata.forward(3*x*math.sqrt(2)/2)
tata.left(90)
tata.forward(3*x*math.sqrt(2)/2)
tata.left(135)
tata.forward(x/2)
tata.forward(2*x)
tata.end_fill()
turtle.done()

