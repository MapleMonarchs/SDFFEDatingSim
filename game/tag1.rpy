label day_one:

    #Hier ist das Intro irgendwo
    #Also das, wo der Charackter mit dem Auto so rum cruist
    #und dann das Haus findet
    # und das ist nur ein erster Ansatz/ eine Idee
    #na clearomatiko, will es nur hinschreiben :D


    "äh oh gott mir fällt nichts ein" #<- Ist das jetzt ein Platzhalter oder Text? Excellent question, vermutlich nur platzhalter

    "Mit einem lauten Knallen gibt der Motor meines geliebten Autos nun endlich den Geist auf."

    "Nervös schaue ich mich um."

    "Mit zusammengekniffenen Augen kann ich eine Bewegung am seltsamen Haus ausmachen."

    "Im Schutz der Dunkelheit nähert sich eine finstere Gestalt."

    "…. Hilfe."

    show duden_night at left

    d "Guten Abend."

    ###Duden ist hier noch ???

    "Vor Schreck fahre ich zusammen."

    "Meine schwitzenden Hände rutschen an dem Türgriff des Autos ab." 

    "Ich hätte doch einen Apfel zum Frühstück essen sollen. {p}Das habe ich jetzt davon."

    "Die finstere Gestalt schaut mich verwundert an."

    d "Wäre es angemessen für mich, zu fragen, warum Sie uns zu solch später Stunde besuchen?"

    menu:
        "Mein Auto ist zusammengebrochen.":

            d "Ah, ich verstehe. {p}Autos sind auch nicht das, was sie mal waren, nicht wahr?"

            "Mir bleibt nichts anderes übrig, als verblüfft zu nicken."

        "Ich gehe nur spazieren.":
            "Ich schaue die Person vor mir mit verschränkten Armen und lässiger Miene an."
            "Die seltsame Gestalt schaut an meiner Schulter vorbei."
            "Ich drehe mich ebenfalls um."
            "Erst jetzt fällt mir ein, dass mein Auto Rauch spuckend im Regen hinter mir steht."
            "Vermutlich kein so guter erster Eindruck."
        
        "Ich bin mit jemandem verabredet.":
            d "Ah ja."
            d "Natürlich."
            d "Ein normales Treffen, am späten Abend, bei {i}diesem{/i} Wetter? {w}{p}Mit einem hoffnungslos zerstörten Fahrzeug?"
            "Ich fühle mich merkwürdig ertappt." 

    "Die dunkle Person kichert leise."

    d "Jedenfalls, hätten Sie Lust, kurz reinzukommen?"
    d "Raus aus dem Regen zumindest, bis wir eine Lösung gefunden haben."
    d "Ich glaube, ich kenne jemanden, der Ihr Auto wieder hinbekommt."

    menu:
        "Ich folge der Person":
            pass
        
        "Unschlüssig stehen bleiben":
            "Ich bleibe unschlüssig stehen."
            "Die Person bleibt stehen."
            d "Keine Sorge, es wird schon keiner von uns beißen."
            p "{cps=5}...{/cps}{cps=20}Von {i}uns{/i}{/cps}?"
            "Die Person macht eine abwerfende Handbewegung."
            d "Du wirst schon sehen."

        # Multiple Choice (Ja, ich weiß, das sind sehr viele)

        "Der Person zustimmen und folgen":
            "Ich gebe schließlich nach und stimme zu, das Haus zu betreten"

        "Den Vorschlag ablehnen und zum Auto zurückkehren.":
            "Ich lehne den Vorschlag (erneut) ab und gehe zurück zum Auto."
            "Ich versuche den Motor neuzustarten."
            "Vergebens."
            d "Sie {cps=20}. . . {/cps} werden das Fahrzeug vor Sonnenaufgang nicht zum Laufen bekommen."
            "Der Regen wird stärker."
            "Der kalte, Wind zieht unbarmherzig an meiner ohnehin schon vollkommen durchnässten Kleidung."
            "Widerwillig muss ich erkennen, dass sich weigern nichts bringen wird."
            "Ich nicke mit zusammengebissenen Zähnen, {p} und nehme das Angebot an."
            d "Sie werden es nicht bereuen."
            "{cps=20}…{/cps}"
            "Meine Zweifel behalte ich für mich selbst."

    "Die Person winkt mit der Hand, deutet an, ihr zu folgen."
    "Gemeinsam folgen wir der Auffahrt zum Haus."
    "Nur wenige Lampen verstreuen ein gedimmtes, orangenes Licht."
    "Im Garten selbst liegen die skurrilsten Sachen verstreut."
    "Durch die schwache Beleuchtung kann ich jedoch nichts genau identifizieren."
    "Nachdem ich jedoch ein wie eine Bombe geformtes Objekt im Gras liegen sehe, {w}versuche ich, alles so gut wie möglich zu ignorieren."
    "Seltsame Artefakte, Gebäude und sogar Magie sind in dieser Welt nicht wirklich… ungewöhnlich."
    "Trotzdem…"
    "Irgendetwas hier ist anders."
    "Sei es das Gebäude, dass beim Näherkommen mehr oder weniger zusammengeflickt wirkt-"
    "Ganz anders als die meisten Märchenschlösser, die ich soweit kenne-"
    "Oder, dass meine Armbanduhr langsam verrückt spielt."
    "Ich bekomme eine Gänsehaut."

    d "Ich unterbreche nur ungern ihren inneren Monolog, aber …"
    "Die Person räuspert sich."
    d "Dürfte ich ihren Namen erfahren, wenn es ihnen nicht zu privat ist?"

    #Multiple CHoice

    menu:
        "Ja":   
            label NameCalling:
                $ name = renpy.input("Wie möchtest du genannt werden?", length=32)
                $ name = name.strip()

        "Sollten sie sich nicht zuerst vorstellen?":
            d "Selbstverständlich, verzeihen sie meine Unhöflichkeit."
            d "Mein Name ist Dr. Duden."
            p "Duden? Wie das Wörterbuch?"

            $ d_names[0] = d_names[1]

            d "Korrekt."
            d "Und ihr Name ist…?"
            jump NameCalling


        "Mir ist es etwas zu privat.":
            d "Das werde ich respektieren müssen, schätze ich."
            d "Haben sie stattdessen eine Art Spitzname, den sie genannt werden wollen?"
            d "Es wäre höchst umständlich, sie die ganze Zeit {w}\"Fremder\"{w} vor den Anderen nennen zu müssen."
            p "Andere?"
            "Die Person seufzt."
            d "Ich befürchte, sie werden sie früh genug kennenlernen."
            "Das klingt nicht wirklich beruhigend."
            p "Nennen sie mich einfach…"

            jump NameCalling

    d "[name], ein passender Name, wenn ich so sagen darf."
    "Was auch immer das heißen soll."

    if d_names[0] != d_names[1]:
        d "Da fällt mir ein, mein Name ist Dr. Duden."
        p "Duden? Wie das Wörterbuch?"

        $ d_names[0] = d_names[1]

        d "Korrekt."
        d "Seien Sie beruhigt, es wird in Zukunft mehr Sinn ergeben."
        p "Ähh, ok."

    scene front_door

    show duden_night at left

    "Ich schaue nach vorne."
    "Inzwischen sind wir an dem Gebäude angekommen, und stehen nun vor einer großen, hölzernen Tür."
    "Der Weg hatte sich {i}deutlich{/i} länger angefühlt, als er ursprünglich aussah."
    "Mein Auto wurde schon längst von der Dunkelheit verschluckt, ich kann es von hier nicht mehr sehen."
    "Ein lautes Klimpern lässt mich erschrocken auffahren."
    d "Ach, Verzeih."
    d "Ich weiß nur nicht, wo ich meine Schlüssel gelassen habe."
    d "Nur eine Sekunde, ich habe sie gleich-"

    menu:
        "Geduldig warten":
            pass

        "Nach den anderen Bewohnern des Hauses fragen.":
            p "Wohnen hier nicht auch noch andere Menschen?"
            p "Wir könnten auch einfach klingeln."
            "Duden unterbricht die Sucherei und schaut zu mir."
            d "Dies ist zwar korrekt, hier leben Personen, aber…"
            "Duden greift seufzend in die Tasche."
            d "Vielleicht schlafen einige schon, {p} ich habe kein Bedürfnis, sie zu wecken."

        "Sehr Akward Smalltalk anfangen":
            p "Also.. Äh…"
            p "Schöne Bomben im Garten."
            "Duden dreht sich verdutzt zu mir um."
            "Das könnte vielleicht der falsche Konversationsstarter gewesen sein."
            p "Ich meinte… {cps=15}äh . . . {/cps} interessanter Garten."
            p "Sind sie Gärtner?"
            d "...Nein."
            d "Nicht wirklich."
            d "Unsere, sagen wir mal {i}ausgefallene{/i} Dekoration haben wir Vani zu verdanken."
            p "...Vani?"
            d "Wenn du Glück hast, wirst du sie in ihren guten Momenten treffen."
            p "…"
            p "Sicher, dass es in Ordnung ist, wenn ich reinkomme?"
            d "Selbstverständlich, absolut kein Problem."
            p "Die Bomben sind nicht echt, oder?"
            "Duden schaut verlegen zur Seite." 
            d "...Nein."
            "Ich entscheide mich, nicht weiter nachzuhaken."
            $ vani = True

    "Ein seltsames Schweigen breitet sich zwischen uns Beiden aus."
    d "…"
    d "Ha!"

    "Duden streckt stolz einen irritierend großen Schlüssel in die Höhe."
    "Endlich."

    "Mit einem lauten Quietschen lässt sich die Tür nun endlich öffnen."
    "Duden schaut zu mir, nickt, und schreitet durch den Eingang."
    "Es bleibt mir nichts anderes übrig als zu folgen."

    scene indoors

    "Vor mir erstreckt sich eine riesige, warm beleuchtete Halle."
    "Zu meiner Enttäuschung ist die Halle fast noch seltsamer als der Garten."
    "… Ist das ein Baum im Gang?"
    d "Willkommen in unseren bescheidenen Zuhause."
    "Ich drehe mich zu Duden.s"
    
    show rsz_duden_half at left

    "Mir ist nichtmal aufgefallen, dass der Doktor weiblich ist."
    "Wow."
    "Meine Auffassungsgabe ist echt beschissen."
    p "Es ist…"

    menu:

        "Schön":
            pass
        "Interessant":
            pass
        "Seltsam":
            pass

    #Ja, die Antwort ist immer die Gleiche

    d "Ach, das ist lieb von dir."
    d "Aber wir könnten hier auch gerne mal wieder aufräumen."
    "Sie wirft mir einen entschuldigenden Blick zu."
    d "Wir haben nur keinen plötzlichen Besuch erwartet."
    p "Kann ich verstehen."
    

    "Wow, ich kann den schüttenden Regen selbst von hier drinnen hören."
    "Trotz des brennenden Lichtes kann ich kein weiteres menschliches Wesen sehen."
    "Eine Katze streift im Halbdunkel entlang."
    "Eine Andere starrt mich aus einen der vielen Gänge an."
    "Vielleicht ist Duden auch nur eine verrückte Katzenlady."
    "Ich nicke, als sich bei mir innerlich die Puzzleteile zusammenfügen."
    "Es gibt vermutlich keine \"Anderen\", nur eine große Menge an Haustieren."
    "Sie ist vermutlich einfach sehr einsam." 
    "… Auch wenn das nicht die äußerst ungewöhnliche Außengestaltung des Gartens  und des Innenraums erklärt."
    "...Nun, im Land der Fanfictions bin ich schon seltsameren Dingen begegnet."
    "Duden räuspert sich."
    d "Ich möchte nicht ihren inneren Monolog unterbrechen,"
    d "Aber möchten Sie vielleicht etwas Essen oder Trinken?"

    menu:

        "Ja":
            "Duden reicht mir eine Flasche Wasser und eine Dose Kekse."

            #Ein kleines Pop-Up an der Seite erscheint "1x Wasser wurde zum Inventar hinzugefügt."
            #"1x Kekspackung wurde zum Inventar hinzugefügt."

            p "Danke."
            d "Kein Problem."

        "Nein":
            d "Sicher?"
            d "Na dann."

    d "Ah, da fällt mir ein:"
    d "Wir haben noch einige Zimmer frei."
    d "Zumindest seit … Ach egal."

    p "Hm…?"

    d "Nun, möchten Sie vielleicht bei uns übernachten?"
    d "Nur, bis Ihr Auto repariert ist."
    d "Es hat zu dieser Uhrzeit keine Werkstatt mehr offen, {w}und ich habe keinen Bedarf zu sehen, wie Sie sich eine Erkältung holen."

    "Ich schaue durch eines der Fenster nach draußen."
    "Der Sturm sieht in der Tat sehr ungemütlich aus."
    "Bei meinem Auto bekomme ich auch bestimmt nicht mehr die Heizung an."
    "Also. welche Wahl habe ich?"
    "Ich stimme zu."

    "Duden nickt zustimmend."

    d "Dann wäre das auch abgeschlossen."
    d "Dein Zimmer liegt direkt im Gang geradeaus, du kannst es nicht verfehlen."
    #Du hast 1x Zimmerschlüssel erhalten
    d "Mein Zimmer liegt im rechten Korridor, falls du etwas brauchst."
    d "Wecken Sie mich ruhig, falls Sie etwas benötigen."
    
    menu:

        "Danke.": 
            d "Keine Ursache."
            d "Ich helfe, wo ich kann."

        "Gute Nacht.":
            d "Oh, vielen Dank."

        "Warum sind Sie so freundlich?":
            d "Nun…"
            "Duden macht eine verlegene Pause."
            d "Wir bekommen nicht viel Besuch."
            d "Und ich muss auch gestehen... {p}Mir ist langweilig."
            d "Ich habe nicht viel zu tun."
            p "Wollen Sie damit sagen, dass Sie mich hätten draußen stehen lassen, {w}wenn Ihnen nicht ...langweilig wäre?"
            d "{cps=20}...{/cps}Korrekt."
            "Oh man."
    
    d "Nun, ich wünsche Ihnen eine angenehme Ruhe in unseren bescheidenen Zuhause."

    #NOW GOING TO ROOM IDK HOW TO DESCRIBE IT FAKE THAT IS YOUR DOING
    #TODO: RAYCASTING-STUFF

    pass

    #JAAAAASSSSSSSSSSSSS
    #:D


    #DAY 1 OVER
    #DAY 2 STARTS

    
