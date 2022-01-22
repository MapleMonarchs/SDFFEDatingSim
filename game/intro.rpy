image lightning:
    linear .09 alpha 1
    parallel:
        choice:
            "intro/lightning1.png"
        choice:
            "intro/lightning2.png"
        choice:
            "intro/lightning1.png"
    parallel:
        choice:
            pause .1
        choice:
            pause .2
        choice:
            pause .3
        choice:
            pause .4
        choice:
            pause .5

    linear .09 alpha 0
    pause .6
    repeat

transform t_trans:
    ypos 400
    xpos 500

transform c_trans:
    choice:
        ypos 400
        xpos 500
    choice:
        ypos 500
        xpos 400
    choice:
        ypos 300
        xpos 400
    choice:
        ypos 500
        xpos 600
    choice:
        ypos 490
        xpos 500
    choice:
        ypos 400
        xpos 590

style t_style is text:
    color '#ffff'
    font "fonts/Itim-Regular.ttf"
    size 30

style c_style is text:
    color '#eee9cc'
    font "fonts/Anton-Regular.ttf"
    size 42
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]


###################################################################################################

#THE INTRO
label intro:

    scene intro_road
    with fade

    image intro_anim    = Movie(play="images/intro/Intro.webm")
    image thoughts       = ParameterizedText(style="t_style")
    image credits       = ParameterizedText(style="c_style")
    image title         = Image("images/intro/Titel.png", size=0.5)

    ###############################################################################################

    show title at center with dissolve

    $ renpy.pause(2)

    show intro_anim with dissolve

    play music "audio/driving.mp3"

    #just for aestheticcs
    $ renpy.pause(1)

    show credits "Programming:\nFake" at c_trans with dissolve
    $ renpy.pause(3)
    show credits "Sprite Art:\nDuden" at c_trans with dissolve
    $ renpy.pause(3)
    show credits "Background Art:\nVani" at c_trans with dissolve
    $ renpy.pause(3)
    show credits "Additional Art:\nTerra, Luca" at c_trans with dissolve
    $ renpy.pause(3)
    show credits "Script & Directing:\nDuden, Vani, Luca, Terra, Fake" at c_trans with dissolve
    $ renpy.pause(3)
    show credits "Emotional Support:\nHestia, Maarlin, Luca" at c_trans with dissolve
    $ renpy.pause(3)

    hide credits with dissolve


    $ renpy.pause(3)

    ###############################################################################################

    show thoughts "Es war eine wunderschöne Nacht in Wattpadien." at t_trans with dissolve
    $ renpy.pause()
    show thoughts "TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT" at t_trans
    $ renpy.pause()
    show thoughts "Doch - natürlich - hatte mein Audi R8™ eine Panne." at t_trans
    $ renpy.pause()

    hide thoughts with dissolve

    stop music fadeout 1.0

    ###############################################################################################

    image black = "#000"

    scene black with Fade(0.5, 1.0, 0.5)
    show lightning
    show intro_house_l    

    play music "audio/thunder.mp3" fadein 2.5

    "Vor diesem seltsamen Horrorhaus." 
    

    "Und zwar irgendwo im Nirgendwo."

    #der Befehl zum Stoppen von "thunder.mp3" (stop music fadeout 1.0) ist in script.rpy
