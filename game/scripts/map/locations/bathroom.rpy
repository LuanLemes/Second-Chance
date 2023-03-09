screen bathroom():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Hallway")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Hallway")
        text "Living Room" xpos 0.5 xanchor 0.5 ypos 0.955 color "#fff"

        imagebutton auto "overlays/toilet_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            # hovered SetVariable("focus_location", "Martha Room")
            # unhovered SetVariable("focus_location", location_object.name)
            action Call("toilet")
        imagebutton auto "overlays/sink_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            # hovered SetVariable("focus_location", "Martha Room")
            # unhovered SetVariable("focus_location", location_object.name)
            action Call("sink")

        imagebutton auto "overlays/shower_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            # hovered SetVariable("focus_location", "Martha Room")
            # unhovered SetVariable("focus_location", location_object.name)
            action Call("shower")
    use top_screen


label bathroom:
    window hide
    if bathroom_first == True:
        $ peed = False
        $ bathed = False
        $ brushed = False
    default bathroom_exit_dialogue = []
    default exit_dialog = ""
    return


label bathroom_on_exit:
    if bathroom_first == True:
        $ bathroom_exit_dialogue = []
        $ exit_dialog = ""

        if peed == False:
            $ bathroom_exit_dialogue.append("(I need to pee)")

        if bathed == False:
            $ bathroom_exit_dialogue.append("(I'm Stinking I need to take a shower first.)")
            $ bathroom_exit_dialogue.append("(I need to take a shower before I go out.)")

        if brushed == False:
            $ bathroom_exit_dialogue.append("(I can't go out with a bad breath.)")

        if bathroom_exit_dialogue != []:
            $ exit_dialog = renpy.random.choice(bathroom_exit_dialogue)
            mc_thought "[exit_dialog]"
            return False
        else:
            $ bathroom_first = False
            $ school_prepare = True
            return True

    window hide
    return


label toilet:
    if peed == True:
        mc_thought "(I dont need to do that anymore)"
        return
    mc_thought "(Oh man much better.)"
    $ peed = True
    return


label shower:
    if bathed == True:
        mc_thought "(I dont need to do that anymore)"
        return
    show black with dissolve
    mc_thought"(So today is the first day of college.)"
    mc_thought"(Seems like just yesterday. I first set foot here for the first time.)"
    mc_thought"(My own disfunctional family, even if we aren't blood related.)"
    mc_thought"(I woulden't have gotten to where I'am whitout them.)"
    $ bathed = True
    hide black with dissolve
    return


label sink:
    if brushed == True:
        mc_thought "(I dont need to do that anymore)"
        return
    mc_thought"(My breath is better now.)"
    $ brushed = True
    return
