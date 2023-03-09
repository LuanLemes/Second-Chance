screen laundry_room():

    frame:

        xalign 0.0
        yalign 0.0

        xsize 1920
        ysize 1080

        background (str(map_image))

        imagebutton auto "overlays/laundry_click_%s.webp":
            focus_mask True
            xpos -5
            ypos -5
            hovered SetVariable("focus_location", "Bathroom")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("laundry_click")
        imagebutton:
            xpos 0.5
            xanchor 0.5
            ypos 0.95
            hover im.Scale("gui/idle.png", 340, 47)
            idle im.Scale("gui/hover.png", 340, 47)
            hovered SetVariable("focus_location", "Living Room")
            unhovered SetVariable("focus_location", location_object.name)
            action Call("change_location_to", "Living Room")
        text "Living Room" xpos 0.5 xanchor 0.5 ypos 0.955 color "#fff"
    use top_screen





label laundry_room:
    return

label laundry_click:
    $phrase = renpy.random.choice(laundry_click_phrases)
    mc_thought "([phrase])"