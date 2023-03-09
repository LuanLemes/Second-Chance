label mandy_relations:
    scene hallway morning:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(0.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    show mandy default:
            xpos 500 xzoom 0.75 yzoom 0.75 
    with dissolve




    "This is {color=#857AFF}Mandy {/color}. She will be living with you during the game, but what is she to you?"
    $ manmc = renpy.input("Mandy is your?", length = 14, default = "Bestie")
    $ mcman = renpy.input("And you are her?", length = 14, default = "friend")
    menu:
        "So she is your {color=#857AFF}[manmc] {/color}and you are her {color=#857AFF}[mcman]{/color} is that right?"
        "Yes":
            "Alright!"
        "No":
            "Lets fix that them."
            call mandy_relations
    hide mandy angry
    with dissolve
    hide hallway morning
    show hallway morning
    return


label martha_relations:
    "This is Martha. She will be living with you during the game, but what is she to you?"
    $ marmc = renpy.input("Martha is your?", length = 14, default = "friend")
    $ mcmar = renpy.input("And you are her?", length = 14, default = "friend")
    menu:
        "So she is your {color=#857AFF}[marmc] {/color}and you are her {color=#857AFF}[mcmar]{/color} is that right?"
        "Yes":
            "Alright!"
        "No":
            "Lets fix that them."
            call martha_relations


label ana_relations:
    "This is Ana. She will be living with you during the game, but what is she to you?"
    $ anamc = renpy.input("Ana is your?", length = 14, default = "friend")
    $ mcana = renpy.input("And you are her?", length = 14, default = "friend")
    menu:
        "So she is your {color=#857AFF}[anamc] {/color}and you are her {color=#857AFF}[mcana]{/color} is that right?"
        "Yes":
            "Alright!"
        "No":
            "Lets fix that them."
            call ana_relations


label agatha_relations:
    "This is Agatha. She will be living with you during the game, but what is she to you?"
    $ agamc = renpy.input("Agatha is your?", length = 14, default = "friend")
    $ mcaga = renpy.input("And you are her?", length = 14, default = "friend")
    menu:
        "So she is your {color=#857AFF}[agamc] {/color}and you are her {color=#857AFF}[mcaga]{/color} is that right?"
        "Yes":
            "Alright!"
        "No":
            "Lets fix that them."
            call agatha_relations

label caroline_relations:
    "This is Caroline. She will be living with you during the game, but what is she to you?"
    $ carmc = renpy.input("Caroline is your?", length = 14, default = "friend")
    $ mccar = renpy.input("And you are her?", length = 14, default = "friend")
    menu:
        "So she is your {color=#857AFF}[carinemc] {/color}and you are her {color=#857AFF}[mccar]{/color} is that right?"
        "Yes":
            "Alright!"
        "No":
            "Lets fix that them."
            call caroline_relations
