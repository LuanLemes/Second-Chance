screen martha_room():

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
        text "Hallway" xpos 0.5 xanchor 0.5 ypos 0.955 color "#fff"

label martha_room:
    window hide
    return

label martha_room_on_enter:
    $ cant_enter_mensage = renpy.random.choice(cant_enter_martha_room_phrases)
    mc_thought "[cant_enter_mensage]"
    
return False