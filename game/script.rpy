
image back = 'backs/front_door.png'

init python:
    def custom_quit():
        import random

        quit_strings = [
            "Geh nicht - die Liebe deines Lebens wartet!", 
            "Denkst du, du kannst so einfach gehen?", 
            "Speichern nicht vergessen!", 
            "Nun denn, so schreitet ihr von dannen!",
            "Dann geh doch was besseres tun..."
        ]

        ind = random.randint(0,len(quit_strings)-1)

        config.translations[u'Are you sure you want to quit?'] = u"{}".format(quit_strings[ind])

    custom_quit()

# Hier beginnt das Spiel.
label start:

    call logos from _call_logos

    call intro from _call_intro

    #Hier ist das Intro irgendwo
    #Also das, wo der Charackter mit dem Auto so rum cruist
    #und dann das Haus findet
    # und das ist nur ein erster Ansatz/ eine Idee
    #na clearomatiko, will es nur hinschreiben :D

    $ name = "Ich"
    $ vani = False

    call day_one from _call_day_one

    call day_two
        

    #  d_names[0] = d_names[1] ---> um den Namen dann zu ändern

    #d "Testsssss"

