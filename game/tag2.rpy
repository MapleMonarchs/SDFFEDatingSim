#schwarzer Screen, Vogelgezwitscher, seeehr langsamer Fade-In" Fade(0.5, 10.0, 0.5), oder wie? Ye ZEHN SEKUNDEN???? °^° 
    # Speicherscreen? Bzw. "Möchtest du jetzt speichern" - geht das? Keine Ahnung :)
    #Jedenfalls, weiter im Script

label day_two:

    scene room_tmp

    "Warmes Licht fällt in mein Gesicht."
    "Das leichte Vogelgezwitscher trägt mich sanft aus dem Schlaf."
    "Ich liege bequem umgeben von weichen Kissen und Decken."
    "Wo… wo bin ich?"
    "Ich schaue mich um."
    "Ah ja, stimmt."
    "Ich wurde von einer random Person in ihr Haus gelassen."
    "Einer einsamen, seltsamen Person mit vielen Katzen, welche von sich im Plural spricht."
    "Eine Person, die anscheinend mit imaginären Personen zusammenlebt."
    "Irgendetwas sagt mir, dass ich das Angebot vielleicht nicht hätte annehmen sollen."
    "Ich richte mich auf."

    #SCREEN RAUM KP MAN KANN DAS INVENTAR UNd SO ANGRAPSCHEN/GLUBSCHEN UNd DAS ZIMMER VERLASSEN 
    
    #"Warum ist das Licht bei mir gerade so beschissen…?"

    #Wenn du das Zimmer verlassen willst, fragt er dich, ob du das wirklich willst. Wenn du das akzeptierst, kommt folgender Dialog:

    "Ich stehe auf und gehe zur Tür."
    "In dem Moment, in dem ich zur Türklinke greife, höre ich Geräusche."
    "Die verrückte Dame füttert vermutlich gerade ihre Unmengen an Katzen."
    "… Das würde ich zumindest denken, wenn eine der Stimmen nicht so {i}tief{/i} wäre."
    "Hm. Vielleicht lebt sie doch nicht alleine."
    "Oder wechselt stündlich das Geschlecht."    #die Angst der AfD
    "Wäre zumindest nicht das Verrückteste, was ich bisher gesehen hätte."
    " Ich hoffe, dass \"die Anderen\”, {w}wer auch immer sie sind,{w} wenigstens so freundlich sind wie diese ominöse Duden."
    if vani == True:
        "Ich hoffe auch, dass ich diese Vani, so gut es geht, vermeiden kann."
        "Ich verlasse das Zimmer und gehe zurück zu der Eingangshalle."
    #transition with slow fade in

    "Ich bin… überrascht."
    "Da stehen mehrere Personen."
    "Wow."
    "Zwar umgeben von dutzenden Katzen, aber dennoch."
    "Ich reibe mir die Augen."
    "Ursprünglich habe ich geplant, da einfach reinzulatschen und \"Hallo\" zu sagen…"
    "Jetzt bin ich mir jedoch nicht ganz so sicher."

    "Soll ich da wirklich einfach hingehen, oder mich eher im Hintergrund halten?"

    #Multiple Choice:

    menu: 

        "Ich halte mich fürs Erste zurück.":
            "Ich verstecke mich hinter der Ecke."
            "Vielleicht kann ich erstmal hören, worüber sie reden, {w} bevor ich reinplatze."
            "Ich höre Duden etwas sagen."
            d "Ich..." 


        "Ich spaziere da einfach entlang und grüße die mal.":
            "Mit selbstbewussten Schritten gehe ich zu der Gruppe an Menschen."
            "Sofort habe ich ihre Aufmerksamkeit."

        "Ich ahme Katzenmiauen ohne guten Grund nach.":
            p "Miau!"
            "Wie erwartet habe ich sofort die Aufmerksamkeit der Gruppe auf mich gezogen."
            "Äh, was jetzt..?"
            "Ich habe tatsächlich nicht weiter über die Konsequenzen meines Verhaltens nachgedacht."   #r/me_irl #Duden verliert die Fassung Klappe 2 #Och nö
            "Duden geht zu mir, {p} und zieht amüsiert eine Augenbraue hoch."
            d "Du nimmst vermutlich nichts von dem Ganzen hier ernst, {w} oder?"
            "Ich schüttele den Kopf."
            "Ein Schweigen macht die Runde."
            "Duden grinst schließlich, {w} und reckt ihren Daumen in die Höhe."
            d "Gut. Das ist die richtige Einstellung in diesem Haus, befürchte ich."
            f "Befürchten?"
            f "Ich bitte dich, Duden, du bist mindestens genauso schrecklich wie alle anderen auch."
            f "Schlimmer noch, dir scheint es sogar zu {i}gefallen{/i}."
            d "Verzeihung?"
            "Die gehörnte Person nickt zustimmend."
            v "{i} Du{/i} machst sogar fast noch schlimmere Wortwitze als ich."
            v "...Aber nur fast."
            d "Ihr gebt unserem Gast ein vollkommen falsches Bild von mir!"
            f "Tja, das nennt man Service."
            "Wo bin ich hier gelandet?"
            "Duden verdreht die Augen und wendet sich wieder zu mir."





    d "...Das wäre dann der Besuch, von dem ich gesprochen hatte."
    d "Der Name ist [name], {w} falls sich einer von euch gefragt hatte."
    "Erst jetzt fallen mir die anderen Personen auf."
    "Sie sehen fast so absurd aus wie Duden."
    v "...Duden, keiner hat gefragt."
    "Skeptisch werde ich von ihren roten Augen betrachtet."
