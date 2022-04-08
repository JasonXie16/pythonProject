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
    höchsterY = rechteck1[3]
    niedrigsterY = rechteck1[1]
    höchsterX = rechteck1[2]
    niedrigsterX = rechteck1[0]
    rechteck2Y2 = rechteck2[3]
    rechteck2X2 = rechteck2[2]
    Rechteck2X1 = rechteck2[0]
    Rechteck2Y1 = rechteck2[1]
    #Fall1:Obern rechte ecke vom Rechteck2 ist inerhalb Rechteck1
    #Fall2:Unten linke ecke vom Rechteck2 ist inerhalb Rechteck1
    #Fall3:
    #Fall4:
    return (rechteck2Y2 < höchsterY and rechteck2Y2 > niedrigsterY and rechteck2X2 < höchsterX and rechteck2X2 > niedrigsterX) \
            or (Rechteck2X1 < höchsterX and Rechteck2X1 > niedrigsterX and Rechteck2Y1 < höchsterY and Rechteck2Y1 > niedrigsterY) \
            or (Rechteck2X1 < höchsterX and Rechteck2X1 > niedrigsterX and rechteck2Y2 < höchsterY and rechteck2Y2 > niedrigsterY) \
            or (rechteck2Y2 < höchsterX and rechteck2X2 > niedrigsterX and Rechteck2Y1 < höchsterY and Rechteck2Y1 > niedrigsterY) \
            or (rechteck2Y2 > höchsterY and Rechteck2Y1 < niedrigsterY and rechteck2X2 < höchsterX and rechteck2X2 > niedrigsterX) \
            or (rechteck2Y2 > höchsterY and Rechteck2Y1 < niedrigsterY and Rechteck2X1 < höchsterX and Rechteck2X1 > niedrigsterX) \
            or (rechteck2X2 > höchsterX and Rechteck2X1 < niedrigsterY and Rechteck2Y1 < höchsterY and Rechteck2Y1 > niedrigsterY) \
            or (rechteck2X2 > höchsterX and Rechteck2X1 < niedrigsterY and rechteck2Y2 < höchsterY and rechteck2Y2 > niedrigsterY) \


def berechnelandanahme(kordinatenliste):
    dictonary = {}
    for onerechteck in kordinatenliste:
        dictonary[onerechteck]=True
        for vierecke in dictonary.keys():
            Status = hatueberschneidung(vierecke,onerechteck)
            if Status:
                dictonary[onerechteck]=False
                break
    print(dictonary)






Kordinaten = [(2,3,5,5),(1,2,4,4),(3,1,6,3)]


berechnelandanahme(Kordinaten)

