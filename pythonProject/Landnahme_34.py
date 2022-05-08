import turtle
import random
'''
    methode:berechnelandnahme
    eingabe: eine list von kordinaten (set mit 4 int)
    ausgabe: (2,5,4,6) genehmigt/abgelehnt

    Shritt1:
    eine methode zu überprüfen on 2 rechtecke sich überschneiden
    methodename:hatueberschneidung
    eingabe: 2 set/liste mit jeweils 4 int
    ausgabe: true/false

    Schritt2:vergleich ein rechteck mit vorherigen
    dict={(2,5,4,6):true,(5,4,3,3):false}
'''

#dict={(2,3,5,5):True,(3,2,4,4):False}


def hatueberschneidung(rechteck1,rechteck2):
    rechteck1Y2 = rechteck1[3]
    rechteck1Y1 = rechteck1[1]
    rechteck1X2 = rechteck1[2]
    rechteck1X1 = rechteck1[0]
    rechteck2Y2 = rechteck2[3]
    rechteck2X2 = rechteck2[2]
    rechteck2X1 = rechteck2[0]
    rechteck2Y1 = rechteck2[1]
    #Fall1:Obern rechte ecke vom Rechteck2 ist inerhalb Rechteck1
    #Fall2:Unten linke ecke vom Rechteck2 ist inerhalb Rechteck1
    #Fall3:
    #Fall4:
    Fall5and6 = (
                rechteck2Y2 > rechteck1Y2 and rechteck2Y1 < rechteck1Y1 and rechteck2X1 < rechteck1X2 and rechteck2X1 > rechteck1X1)

    result = ( rechteck2X1 < rechteck1X2 and rechteck2X1 > rechteck1X1 and rechteck2Y2 < rechteck1Y2 and rechteck2Y2 > rechteck1Y1) or \
             ( rechteck2X2 < rechteck1X2 and rechteck2X2 > rechteck1X1 and rechteck2Y2 < rechteck1Y2 and rechteck2Y2 > rechteck1Y1) or \
             ( rechteck2X1 < rechteck1X2 and rechteck2X1 > rechteck1X1 and rechteck2Y1 < rechteck1Y2 and rechteck2Y1 > rechteck1Y1) or \
             ( rechteck2X2 < rechteck1X2 and rechteck2X2 > rechteck1X1 and rechteck2Y1 < rechteck1Y2 and rechteck2Y1 > rechteck1Y1) or \
             Fall5and6 or \
             ( rechteck2Y2 > rechteck1Y2 and rechteck2Y1 < rechteck1Y1 and rechteck2X2 < rechteck1X2 and rechteck2X2 > rechteck1X1) or \
             ( rechteck2X2 > rechteck1X2 and rechteck2X1 < rechteck1X1 and rechteck2Y1 < rechteck1Y2 and rechteck2Y1 > rechteck1Y1 ) or \
             ( rechteck2X2 > rechteck1Y2 and rechteck2X1 < rechteck1Y1 and rechteck2Y2 < rechteck1Y2 and rechteck2Y2 > rechteck1Y1) or \
             ( rechteck2X2 > rechteck1X2 and rechteck2X1 < rechteck1X1 and rechteck2Y2 > rechteck1Y2 and rechteck2Y1 < rechteck1Y1)



    return result


def berechnelandanahme(kordinatenliste):
    turtle.hideturtle()
    dictonary = {}
    counter = 0
    for onerechteck in kordinatenliste:
        dictonary[onerechteck]=True
        counter += 1
        for vierecke in dictonary.keys():
            if dictonary[vierecke]:
                Status = hatueberschneidung(vierecke,onerechteck)
                if Status:
                    dictonary[onerechteck]=False
                    break
        turtle.speed(5)
        turtle.penup()
        if Status:
            turtle.color("red")

        else:
            turtle.color("green")

        turtle.right(90)
        turtle.goto(onerechteck[0], onerechteck[1] )
        turtle.pendown()
        turtle.goto(onerechteck[2], onerechteck[1])
        turtle.goto(onerechteck[2], onerechteck[3])
        turtle.goto(onerechteck[0], onerechteck[3])
        turtle.write(counter)
        turtle.goto(onerechteck[0], onerechteck[1])



    print(dictonary)
    turtle.done()


def erstelleRandomViereck():
    x1 = random.randint(-500,500)
    y1 = random.randint(-500,500)
    x2 = x1 + random.randint(100,200)
    y2 = y1 + random.randint(100,200)
    return (x1,y1,x2,y2)

Kordinaten = []
for i in range(1,20):
    Kordinaten.append(erstelleRandomViereck())
Kordinaten = [(210, -498, 321, -313), (-282, -489, -88, -332), (499, -432, 681, -299), (446, -345, 559, -208), (-492, -120, -362, 30), (223, -465, 372, -300), (-497, -310, -381, -185), (495, -342, 672, -159), (-402, 347, -281, 450), (40, -495, 189, -389), (-257, -12, -107, 126), (-187, -115, 2, 69), (-45, -226, 57, -58), (199, 475, 319, 635), (-197, 236, -49, 401), (106, 212, 282, 363), (291, 135, 463, 235), (-441, -100, -338, 78), (112, -325, 302, -201)]
print(Kordinaten)

berechnelandanahme(Kordinaten)

def test_hatueberschneidung():
    #Fall1
    rechteck1 = (0,0,100,100)
    rechteck2 = (80,-200, 300,40)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall2
    rechteck1 = (0,0,100,100)
    rechteck2 = (-100,-100,20,20)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall3
    rechteck1 = (0,0,100,100)
    rechteck2 = (80,80,200,200)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall4
    rechteck1 = (0, 0, 100, 100)
    rechteck2 = (-70,70,30,200)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall5
    rechteck1 = (0, 0, 100, 100)
    rechteck2 = (50,-200,70,300)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall6
    rechteck1 = (0, 0, 100, 100)
    rechteck2 = (50, -200, 200, 300)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall7
    rechteck1 = (0, 0, 100, 100)
    rechteck2 = (-50, -200, 50, 300)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall8
    rechteck1 = (0, 0, 100, 100)
    rechteck2 = (-200,20,150,50)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall9
    rechteck1 = (50,-200,200,300)
    rechteck2 = (0, 0, 100, 100)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall10
    rechteck1 = (-50,-200,50,300)
    rechteck2 = (0, 0, 100, 100)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall11
    rechteck1 = (0,0,100,100)
    rechteck2 = (-200,-20,150,50)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall12
    rechteck1 = (0, 0, 100, 100)
    rechteck2 = (-100,-100,200,200)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    #Fall13
    rechteck2 = (0, 0, 100, 100)
    rechteck1 = (-100, -100, 200, 200)
    assert hatueberschneidung(rechteck1, rechteck2) == True
    # Fall15
    rechteck2 = (-497, -310, -381, -185)
    rechteck1 = (-492, -120, -362, 30)
    assert hatueberschneidung(rechteck1, rechteck2) == False