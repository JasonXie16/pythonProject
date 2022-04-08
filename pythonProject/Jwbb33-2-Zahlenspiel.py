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




def bruchgenerien(schwierigkeitsgrad):
        Anzahlvonbrüchen = []
        bruch = []
        if schwierigkeitsgrad == "leicht":
            p = random.randint(1,8)
            if p == 8:
                q = 1
            else:
                q = random.randint(1,9 - p )

            faktor = random.randint(2, 11)
            a = p * faktor
            if len(str(a)) == 1:
                while len(str(a)) == 1:
                    faktor = random.randint(2, 11)
                    a = p * faktor

            b = q * faktor

        bruch = [p,q," ",a,b]
        if a == b:
            bruch = bruchgenerien(schwierigkeitsgrad)

        else:
            Anzahlvonbrüchen.append(bruch)
            return Anzahlvonbrüchen













for i in range(0,8):
    print(bruchgenerien("leicht"))






