import random
'''
<ul>
    <li>Schritt:Eine methode schreiben um Brüche zu generien.</li>
    <ul>
        <li>Input:Schwierigkeit, Bsp:"leicht"</li>
        <li>Output:Bruch, Bsp:44/55</li>
    </ul>

    <li>Schritt:Eine methode schreiben die Brüche kürzt.</li>
    <ul>
        <li>Input:Bruch, Bsp:44/55</li>
        <li>Output:Gekürzten Bruch, Bsp: 4/5</li>
    </ul>
    <li>Schritt:Vorherige Schritte für gegebene Anzahl wiederholen</li>
    <ul>
        <li>Input:Anzahl,Schwierigkeit</li>
        <li>Output:Mehrere Brüche und gekürzte Brüche</li>
    </ul>



    Stufe Länge von a /b Bedingung für p /q
    leicht 4 p+q ≤ 10
    mittel 5 10 < p+q ≤ 20
    schwer 5 20 < p+q ≤ 30

'''


def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False


def bruchgenerien(schwierigkeitsgrad):
    bruch = []
    bruch = set(bruch)
    if schwierigkeitsgrad == "leicht":
        a = random.randint(10,99)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)
    elif schwierigkeitsgrad == "mittel":
        a = random.randint(100, 999)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)

    elif schwierigkeitsgrad == "schwer":
        a = random.randint(100, 999)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)

    return bruch


def bruchkuerzen(bruch):
    print(type(bruch))
    bruch = list(bruch)
    print(type(bruch))
    groeßtezahl = 0
    gekürzterbruch = []

    if bruch[0] < bruch[1]:
        kleinstezahl = bruch[0]
    else:
        kleinstezahl = bruch[1]
    print(bruch)
    for i in range (2,kleinstezahl):

        if is_integer_num(bruch[0] / i) and is_integer_num(bruch[1] / i) == True:
            if groeßtezahl < i:
                groeßtezahl = i
    print(str(groeßtezahl) + " Zahl")
    if not groeßtezahl == 0:
        gekürzterbruch.append(bruch[0] / groeßtezahl)
        gekürzterbruch.append(bruch[1] / groeßtezahl)
    else:
        print("bruch ist nicht kürzbar")




    bruch = set(bruch)


print(bruchgenerien("x"))
print(bruchkuerzen(bruchgenerien("leicht")))


